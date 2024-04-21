import sys
import requests
import re
from send_email import send_email
from constants import *


def validate_topic(topic):
    # Strip leading and trailing whitespace from topic
    topic = topic.strip().lower()

    # validate the topic
    if not re.match(TOPIC_PATTERN, topic):
        # Print an error message if the topic is not valid
        print("\n--- Please enter a meaningful topic. For example: 'tesla', 'sports', 'politics', 'bitcoin', etc. ---\n")
        return False

    # Return True if topic is valid
    return True


def validate_langauge(language):
    # Strip leading and trailing whitespace from language
    language = language.strip().lower()

    # validate the language
    if not re.match(LANGUAGE_PATTERN, language):
        # Print an error message if the language is not valid
        print("\n--- Please enter a language code in ISO format (e.g., 'en' for English). ---\n")
        return False

    # Return True if language is valid
    return True


def main(topic=None, language=None):
    # Check if the topic argument is provided, otherwise prompt the user to input a topic
    if topic is None:
        topic = input(
            "\n--- Please enter a topic you want to get news about:  ").strip().lower()

    # Check if the language argument is provided, otherwise use the default language specified in the constants
    if language is None:
        language = input(
            "\n--- Enter a language code in ISO format (e.g., 'en' for English):  ").strip().lower()

    # Make a GET request to the News API to fetch news articles related to the specified topic with parameters ('q' , 'language', and 'apiKey')
    try:
        response = requests.get(f"{NEWS_API_ENDOINT_EVERYTHING}?q={
                                topic}&language={language}&apiKey={NEWS_API_KEY}")
        response.raise_for_status()  # Raise an HTTPError for bad response status codes
    except requests.exceptions.RequestException as e:
        sys.exit(f"\n--- Failed to fetch news articles: {e} ---\n")

    # Using `request.json()` is better to access data using familiar Python syntax, such as dictionary keys and list indices than using `request.text` which is a plain string (str type)
    content = response.json()

    # Check if the response contains valid data
    if 'articles' not in content:
        sys.exit(
            "\n--- No articles found for the provided topic/language. Please try again. ---\n")

    # define the text block of all articles to be sent by email and total number of articles
    all_articles_data = ""

    # Use Debugging mode to monitor data variables and how they are structures (specially lists and dicts) so we know articles are stored in dict content of key 'articles' and same thing for 'title' and 'description'
    # use the get() with dict to avoid raising an error if key not found, so the default value here returned is [] and slicing on [] returns []
    # Limit to the first 20 articles
    for article in content.get('articles', [])[:20]:
        # here no need to define default value wth get() cz if key not found None returned and below the condition filters articles with None data
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')

        # Check if necessary data is available
        if title and description and url:
            # Add all three article data to text block by concatenation
            all_articles_data += f"{title}:\n{description}\n{url}\n\n"

    # check if the text block isnt empty in order to send it by email
    if all_articles_data.strip():
        # send an email of all these articles text block and handle the outcome
        subject = f"{topic.title()} News: The Latest Updates and Headlines"
        if send_email(all_articles_data, subject):
            sys.exit("\n--- Email sent successfully ---\n")
        else:
            sys.exit("\n--- Failed to send email. Please try again later ---\n")
    else:
        sys.exit(
            "\n--- No articles found for the provided topic. Please try again. ---\n")


# Check if the script is being run as the main program
if __name__ == "__main__":
    
    if len(sys.argv) == 3:
        # If the number of command-line arguments is 3 (script name, topic, language) and both topic and labguage are valid
        if validate_topic(sys.argv[1]) and validate_langauge(sys.argv[2]):
            # call the main function with the provided topic and language arguments
            main(topic=sys.argv[1], language=sys.argv[2])
        else:
            # If the provided topic and language do not pass the validation, exit with message
            sys.exit("\n--- Invalid topic or language. ---\n")

    elif len(sys.argv) == 2:
        # If the number of command-line arguments is 2 (script name, topic) and topic is valid
        if validate_topic(sys.argv[1]):
            # call the main function with the provided topic and default language arguments
            main(topic=sys.argv[1], language=DEFAULT_LANGUAGE)
        else:
            # If the provided topic does not pass the validation, exit with message
            sys.exit("\n--- Invalid topic. ---\n")

    # If the number of command-line arguments is not 3, call main() with 'en' as default language arg, prompting the user to enter a topic interactively  
    else:
        main(language=DEFAULT_LANGUAGE)
