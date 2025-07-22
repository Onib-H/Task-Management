from flask import Blueprint, jsonify
from flask_bcrypt import Bcrypt
import base64

admin = Blueprint('admin', __name__)

@admin.route('/', methods=['GET'])
def get_message():
    return jsonify({
        "message": "Hello, Task Management"
    }), 200