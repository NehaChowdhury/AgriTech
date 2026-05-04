import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "AgriTech API"
    DEBUG: bool = True
    
    # Paths
    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    MODEL_PATH: str = os.path.join(BASE_DIR, 'models', 'crop_model.pkl')
    DATA_PATH: str = os.path.join(BASE_DIR, 'data', 'fertilizer.csv')
    STATIC_DIR: str = os.path.join(BASE_DIR, 'static')
    TEMPLATE_DIR: str = os.path.join(BASE_DIR, 'templates')

    class Config:
        env_file = ".env"

settings = Settings()
