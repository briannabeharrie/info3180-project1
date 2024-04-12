import os
from dotenv import load_dotenv
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.env')
load_dotenv()

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER')
    
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace('postgres://', 'postgresql://')
    SQLALCHEMY_TRACK_MODIFICATIONS = False 

    # Mail server configuration
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'sandbox.smtp.mailtrap.io') 
    MAIL_PORT = os.environ.get('MAIL_PORT', '25') 
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', '2e299f2fb8e36b')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', '179de5853142a8')
