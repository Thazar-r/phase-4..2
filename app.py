from flask import Flask
from config import Config
from models import db
from routes import api_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    
    with app.app_context():
        db.create_all()  # Create database tables

    # Register routes
    app.register_blueprint(api_blueprint)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=5555, debug=True)
