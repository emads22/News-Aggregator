import requests
from send_email import send_email
import os
from dotenv import load_dotenv


def main():
    # Load environment variables from the .env file
    load_dotenv()

    # Define the endpoint and API key for the News API, and the topic we want to search for news
    NEWS_API_ENDOINT_EVERYTHING = "https://newsapi.org/v2/everything"
    NEWS_API_KEY = os.getenv("NEWS_apiKey")
    TOPIC = "tesla"
    LANGUAGE = "en"

    # Make a GET request to the News API to fetch news articles related to the specified topic wth parameters ('q' , 'language', and 'apiKey')
    response = requests.get(f"{NEWS_API_ENDOINT_EVERYTHING}?q={TOPIC}&language={LANGUAGE}&apiKey={NEWS_API_KEY}")
    # Using `request.json()` is better to access data using familiar Python syntax, such as dictionary keys and list indices than using `request.text` which is a plain string (str type)
    content = response.json()

    # define the text block of all articles to be sent by email and total number of articles 
    all_articles_data = ""
    total_articles = 0

    # Use Debugging mode to monito data variables and how they are structures (specially lists and dicts) so we know articles are stored in dict content of key 'articles' and same thing for 'title' aand 'description'
    for article in content['articles'][:20]: # only collect the 20 first articles
        # Check if title is not None
        if article['title'] is not None:
            # Create a text block containing title, description of each article of the topic selected and concatenated to all articles text block
            all_articles_data += f"""
{article['title']}:
{article['description']}
{article['url']}

"""         

    # send an email of all these articles text block and handle the outcome
    subject = f"{TOPIC.title()} News: The Latest Updates and Headlines"
    if send_email(all_articles_data, subject):
        print("\n--- Email sent successfully ---\n")
    else:
        print("\n--- Failed to send email. Please try again later ---\n")


if __name__ == "__main__":
    main()