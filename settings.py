# settings.py
import os
from dotenv import load_dotenv

# Explicitly load .env file
load_dotenv()

class Config(object):
    TESTING = os.getenv('TESTING', 'testing')
    YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY', 'Default Value')

