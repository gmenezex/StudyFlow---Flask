from flask import Flask
import os
from dotenv import load_dotenv
from app.extensions import db



load_dotenv()

def create_app():
  
  app = Flask(__name__)
  
  app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///studyflow.db'
  db.init_app(app)
  from app import models

  from app.routes import routes_bp
  app.register_blueprint(routes_bp)
  with app.app_context():
    db.create_all()
  return app