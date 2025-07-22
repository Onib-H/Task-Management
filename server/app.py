from flask import Flask
from flask_mail import Mail
from flask_cors import CORS
from task_management import create_app

app = create_app()

CORS(app, supports_credentials=True)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)