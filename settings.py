import os
from dotenv import load_dotenv

# Explicitly load .env file
load_dotenv()

class Config(object):
    TESTING = os.getenv('TESTING', 'testing')
    YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY', 'Default Value')
    SUPABASE_URL = os.getenv('SUPABASE_URL', 'Your Supabase URL Default')
    SUPABASE_KEY = os.getenv('SUPABASE_KEY', 'Your Supabase Key Default')
    AUTH_TOKEN = os.getenv('AUTH_TOKEN')

