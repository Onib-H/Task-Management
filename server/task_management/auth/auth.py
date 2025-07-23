from flask import Blueprint, jsonify, request
from flask_bcrypt import Bcrypt
from models import init_models
from datetime import datetime, timedelta
from functools import wraps
import sys, os, jwt

auth = Blueprint('auth', __name__)
bcrypt = Bcrypt()

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)
JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)

db = None
User = None
Task = None

def init_auth(database):
    global db, User, Task
    db = database
    User, Task = init_models(db)
    
def generate_tokens(user_id):
    access_payload = {
        'user_id': user_id,
        'exp': datetime.now() + JWT_ACCESS_TOKEN_EXPIRES,
        'iat': datetime.now(),
        'type': 'access'
    }

    refresh_payload = {
        'user_id': user_id,
        'exp': datetime.now() + JWT_REFRESH_TOKEN_EXPIRES,
        'iat': datetime.now(),
        'type': 'refresh'
    }

    access_token = jwt.encode(access_payload, JWT_SECRET_KEY, algorithm='HS256')
    refresh_token = jwt.encode(refresh_payload, JWT_SECRET_KEY, algorithm='HS256')

    return access_token, refresh_token

def verify_token(token, token_type='access'):
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=['HS256'])
        if payload['type'] != token_type:
            return None
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
    
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get('access_token')
        
        if not token:
            return jsonify({'error': 'Token is missing'}), 401
            
        try:
            payload = verify_token(token, 'access')
            if not payload:
                return jsonify({'error': 'Token is invalid or expired'}), 401
                
            current_user = User.query.get(payload['user_id'])
            if not current_user:
                return jsonify({'error': 'User not found'}), 401
                
        except Exception:
            return jsonify({'error': 'Token verification failed'}), 401
            
        return f(current_user, *args, **kwargs)
    return decorated

# /api/** API endpoints
@auth.route('/register', methods=['POST'])
def register():
    if User is None or db is None:
        return jsonify({
            "error": "Database or User model not initialized"
        }), 500
    
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({
                "error": "No input data provided"
            }), 400
            
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        
        if not username:
            return jsonify({
                "error": "Username is required"
            }), 400
        
        if not email or not password:
            return jsonify({
                "error": "Email and password are required"
            }), 400
            
        existing_user = User.query.filter(
            (User.email == email) | (User.username == username)
        ).first()
        
        if existing_user:
            return jsonify({
                "error": "User with this email already exists"
            }), 400
        
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        
        new_user = User(
            username=username,
            email=email,
            password=hashed_password
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({
            'message': 'User registered successfully',
            'user': {
                'id': new_user.id,
                'username': new_user.username,
                'email': new_user.email
            }
        }), 201
    except Exception as e:
        return jsonify({
            "error": f"/api/register POST error: {str(e)}"
        }), 500

@auth.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({
                "error": "No input data provided"
            }), 400
        
        email = data.get('email')
        password = data.get('password')
        
        if not email or not password:
            return jsonify({
                "error": "Email and password are required"
            }), 400
            
        user = User.query.filter_by(email=email).first()
        
        if not user:
            return jsonify({
                "error": "Invalid email or password"
            }), 401
            
        if not bcrypt.check_password_hash(user.password, password):
            return jsonify({
                "error": "Invalid email or password"
            }), 401
        
        access_token, refresh_token = generate_tokens(user.id)    
        
        response = jsonify({
            'message': 'Login successful',
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email
            },
        })
        
        response.set_cookie(
            'access_token',
            access_token,
            max_age=JWT_ACCESS_TOKEN_EXPIRES.total_seconds(),
            httponly=True,
            secure=True,
            samesite='Lax'
        )
        
        response.set_cookie(
            'refresh_token',
            refresh_token,
            max_age=JWT_REFRESH_TOKEN_EXPIRES.total_seconds(),
            httponly=True,
            secure=True,
            samesite='Lax'
        )
        
        return response, 200
    except Exception as e:
        return jsonify({
            "error": f"An error occurred: {str(e)}"
        }), 500

@auth.route('/refresh', methods=['POST'])
def refresh():
    try:
        refresh_token = request.cookies.get('refresh_token')

        if not refresh_token:
            data = request.get_json()
            refresh_token = data.get('refresh_token') if data else None
            return jsonify({
                "error": "Refresh token is required"
            }), 400
        
        payload = verify_token(refresh_token, 'refresh')
        if not payload:
            return jsonify({'error': 'Invalid or expired refresh token'}), 401
        
        user = User.query.get(payload['user_id'])
        
        if not user:
            return jsonify({'error': 'User not found'}), 404
        
        new_access_token, new_refresh_token = generate_tokens(user.id)
        
        response = jsonify({
            'message': 'Access token refreshed successfully',
        })
        
        response.set_cookie(
            'access_token',
            new_access_token,
            max_age=JWT_ACCESS_TOKEN_EXPIRES.total_seconds(),
            httponly=True,
            secure=True,
            samesite='Lax'
        )
        
        response.set_cookie(
            'refresh_token',
            new_refresh_token,
            max_age=JWT_REFRESH_TOKEN_EXPIRES.total_seconds(),
            httponly=True,
            secure=True,
            samesite='Lax'
        )
        return response, 200
    except Exception as e:
        return jsonify({
            "error": f"An error occurred: {str(e)}"
        }), 500

@auth.route('/logout', methods=['POST'])
def logout():
    try:
        if not request.cookies.get('access_token') and not request.cookies.get('refresh_token'):
            return jsonify({'error': 'No authentication cookies found'}), 400

        response = jsonify({'message': 'User logged out successfully'})
        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')
        return response, 200
    except Exception as e:
        return jsonify({
            "error": f"/api/logout POST error: {str(e)}"
        }), 500

@auth.route('/user', methods=['GET'])
def get_user_info(current_user):
    return jsonify({
        'user': {
            'id': current_user.id,
            'username': current_user.username,
            'email': current_user.email
        }
    }), 200
