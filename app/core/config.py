import os

from dotenv import load_dotenv
from pydantic import BaseSettings

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
load_dotenv(os.path.join(BASE_DIR, '.env'))


class Settings(BaseSettings):
    API_PREFIX = ''
    PROJECT_NAME = os.getenv('PROJECT_NAME', '')
    LOGGING_CONFIG_FILE = os.path.join(BASE_DIR, 'logging.ini')
    RUNNING_PORT = os.getenv('RUNNING_PORT', '')
    BACKEND_CORS_ORIGINS = ['*']

    AUTH0_CLIENT_ID = os.getenv('AUTH0_CLIENT_ID', '')
    AUTH0_CLIENT_SECRET = os.getenv('AUTH0_CLIENT_SECRET', '')
    AUTH0_DOMAIN = os.getenv('AUTH0_DOMAIN', '')
    AUTH0_AUDIENCE = os.getenv('AUTH0_AUDIENCE', '')
    AUTH0_BASE_URL = os.getenv('AUTH0_BASE_URL', '')
    AUTH0_ALGO = os.getenv('AUTH0_ALGO', '')

    DOMAIN = os.getenv('DOMAIN', '')
    API_AUDIENCE = os.getenv('API_AUDIENCE', '')
    ALGORITHMS = os.getenv('ALGORITHMS', '')
    ISSUER = os.getenv('ISSUER', '')


settings = Settings()
