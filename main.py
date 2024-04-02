import requests
from send_email import send_email
import os
from dotenv import load_dotenv


# Load environment variables from the .env file
load_dotenv()

# Define the endpoint and API key for the News API, and the topic we want to search for news
NEWS_API_ENDOINT_EVERYTHING = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.getenv("NEWS_apiKey")
TOPIC = "tesla"

# Make a GET request to the News API to fetch news articles related to the specified topic wth arguments ('q' and 'apiKey')
request = requests.get(f"{NEWS_API_ENDOINT_EVERYTHING}?q={TOPIC}&apiKey={NEWS_API_KEY}")
# Using `request.json()` is better to access data using familiar Python syntax, such as dictionary keys and list indices than using `request.text` which is a plain string (str type)
content = request.json()

# Use Debugging mode to monito data variables and how they are structures (specially lists and dicts) so we know articles are stored in dict content of key 'articles' and same thing for 'title' aand 'description'
for article in content['articles']:
    # Create a text block containing title, description, and content - Content: {article['content']}
    article_data = f"""
    - Title: {article['title']}
    - Description: {article['description']}
    
    """
    print(article_data)