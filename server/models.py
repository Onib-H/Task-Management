from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

_User = None
_Task = None

# This will be imported from app.py
def init_models(db):
    global _User, _Task
    
    if _User is not None and _Task is not None:
        return _User, _Task
    
    class User(db.Model):
        __tablename__ = 'users'
        __table_args__ = {'extend_existing': True}
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=True, nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)
        password = db.Column(db.String(200), nullable=False)
        tasks = db.relationship('Task', backref='owner', lazy=True, cascade="all, delete-orphan")
        
        def set_password(self, password):
            self.password = generate_password_hash(password)
            
        def check_password(self, password):
            return check_password_hash(self.password, password)
        
        def __repr__(self):
            return f'{self.username}'
        
    class Task(db.Model):
        __tablename__ = 'tasks'
        __table_args__ = {'extend_existing': True}
        
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(150), nullable=False)
        description = db.Column(db.Text)
        completed = db.Column(db.Boolean, default=False)
        due_date = db.Column(db.DateTime)
        priority = db.Column(db.String(10))
        tags = db.Column(db.String(255))
        created_at = db.Column(db.DateTime, default=datetime.utcnow)
        updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
        user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

        def is_overdue(self):
            return self.due_date and not self.completed and self.due_date < datetime.utcnow()

        def __repr__(self):
            return f"Task {self.title}"
    
    _User = User
    _Task = Task
    
    return User, Task