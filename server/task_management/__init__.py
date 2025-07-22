from flask import Flask
from task_management.admin.sampulan import admin

def create_app():
    app = Flask(__name__)

    app.secret_key = "ket-anu"
    app.register_blueprint(admin, url_prefix="/admin")

    return app