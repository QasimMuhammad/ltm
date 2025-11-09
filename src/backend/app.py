from flask import Flask, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from src.backend.api.routes import api_bp
from src.backend.models.database import init_db

# Load environment variables
load_dotenv()


def create_app():
    """Application factory pattern"""
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret-key-dev-only')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Enable CORS for React frontend
    default_origins = [
        "http://localhost:3000",
        "http://localhost:5173",
    ]

    extra_origins = os.getenv("FRONTEND_ORIGINS")
    if extra_origins:
        default_origins.extend(
            origin.strip()
            for origin in extra_origins.split(",")
            if origin.strip()
        )

    CORS(app, resources={
        r"/api/*": {
            "origins": default_origins,
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"]
        }
    })
    
    # Initialize database
    init_db()
    
    # Register blueprints
    app.register_blueprint(api_bp)
    
    # Root endpoint for API info
    @app.route('/')
    def index():
        return jsonify({
            'service': 'LTM Backend API',
            'version': '0.1.0',
            'endpoints': {
                'health': '/api/health',
                'questions': '/api/questions?type=couple',
                'submit': '/api/responses/couple'
            }
        })
    
    return app


app = create_app()

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
