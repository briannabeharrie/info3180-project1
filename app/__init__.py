from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialise SQLAlchemy
db = SQLAlchemy(app)

# Instantiate Flask-Migrate library
migrate = Migrate(app, db)

# Instantiate Mail
mail = Mail(app)

from app import views