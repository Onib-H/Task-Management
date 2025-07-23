from flask import Flask
from task_management.admin.sampulan import admin
from task_management.auth.auth import auth

def create_app():
    app = Flask(__name__)

    app.secret_key = "ket-anu"
    app.register_blueprint(admin, url_prefix="/admin")
    app.register_blueprint(auth, url_prefix="/api")

    return app