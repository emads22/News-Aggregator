import os
from dotenv import load_dotenv


# Load environment variables from the .env file
load_dotenv()

# Define the endpoint and API key for the News API, and the topic we want to search for news
NEWS_API_ENDOINT_EVERYTHING = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.getenv("NEWS_apiKey")
SENDER_EMAIL = os.getenv("USER")
SENDER_PASSWORD = os.getenv("PASSWORD")
DEFAULT_LANGUAGE = "en"

# Validation patterns
# topic consists of only word characters (letters, digits, and underscores)
TOPIC_PATTERN = r'^\w+$'
# language consists of exactly two lowercase letters
LANGUAGE_PATTERN = r'^[a-z]{2}$'
EMAIL_PATTERN = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
