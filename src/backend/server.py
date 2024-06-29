from flask import Flask
from app.config import Config
from app.db import db
from flask_cors import CORS
from dotenv import load_dotenv
import os


# Initialize Flask app
app = Flask(__name__)

#load client URI and allow CORS for it
load_dotenv()
client_uri = os.getenv('CLIENT_URI')
CORS(app, origins=[client_uri])
#CORS(app, origins="*")

# Load configuration
app.config.from_object(Config)

# Initialize database with the app
db.init_app(app)

# Import models here to avoid circular imports
from app.models.user_model import User

# Create all database tables
with app.app_context():
    db.create_all()

# Import routes here to avoid circular imports
from app.routes.user_routes import user_bp

# Register blueprints
app.register_blueprint(user_bp)

if __name__ == "__main__":
    app.run(debug=True)
