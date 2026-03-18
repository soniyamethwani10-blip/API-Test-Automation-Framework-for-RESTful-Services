import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base Configuration class."""
    ENV = os.getenv("ENV", "qa").lower()
    
    # Base URLs for different environments
    BASE_URLS = {
        "dev": "https://restful-booker.herokuapp.com",
        "qa": "https://restful-booker.herokuapp.com",
        "prod": "https://restful-booker.herokuapp.com"  # Using same URL for demo purposes
    }
    
    BASE_URL = BASE_URLS.get(ENV, BASE_URLS["qa"])
    
    # Credentials
    USERNAME = os.getenv("USERNAME", "admin")
    PASSWORD = os.getenv("PASSWORD", "password123")
    
    # Timeouts
    TIMEOUT = 10
    
    # Retry settings
    RETRY_COUNT = 3
    RETRY_DELAY = 1  # seconds
