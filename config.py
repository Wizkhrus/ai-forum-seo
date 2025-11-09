import os

class Config:
    """Application configuration"""
    # Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///forum.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # OpenAI API
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY') or 'your-api-key-here'
    
    # Forum settings
    FORUM_TITLE = 'AI Forum'
    FORUM_DESCRIPTION = 'Auto-generated community forum'
    
    # Content generation
    MAX_USERS = 120
    INITIAL_THREADS = 20
    CONTENT_GENERATION_INTERVAL = 30  # minutes
    THREAD_CREATION_INTERVAL = 60  # minutes
