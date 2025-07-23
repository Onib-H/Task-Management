from flask_mail import Mail
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy # type: ignore
from flask_migrate import Migrate # type: ignore
from task_management import create_app
from models import init_models
from task_management.auth.auth import init_auth
from dotenv import load_dotenv
import os

load_dotenv()

app = create_app()

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

mail = Mail(app)
db = SQLAlchemy(app)

with app.app_context():
    User, Task = init_models(db)
    init_auth(db)
    
    migrate = Migrate(app, db)
    CORS(app, supports_credentials=True)
    
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)