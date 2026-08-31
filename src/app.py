import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_required_env(name):
    val = os.getenv(name)
    if val is None:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return val

secret_key = get_required_env('SECRET_KEY')
db_user = get_required_env('DB_USER')
db_password = get_required_env('DB_PASSWORD')
db_host = get_required_env('DB_HOST')
db_port = get_required_env('DB_PORT')
db_name = get_required_env('DB_NAME')

from src.coding import web_app  
from src.webservice import api_app  

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key

# Register Blueprints
app.register_blueprint(web_app)
app.register_blueprint(api_app, url_prefix='/api')

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Flask-Migrate for DB migrations

if __name__ == '__main__':
    app.run(debug=True, port=5001)

