# News Aggregator

## Overview
News Aggregator is a command-line tool that fetches news articles from an API based on the user's specified topic and language. It allows users to stay updated with the latest news on various topics.

## Features
- **Topic Validation**: Validates user input to ensure the entered topic is meaningful and relevant.
- **Language Validation**: Validates user input to ensure the entered language code is in ISO format.
- **Fetching News Articles**: Retrieves news articles from an external API based on the user's specified topic and language.
- **Email Notification**: Sends an email containing the fetched news articles to the user's specified email address.

## Setup
1. Clone the repository.
2. Ensure Python 3.x is installed.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Configure the necessary parameters such as `NEWS_API_KEY` and `DEFAULT_LANGUAGE` in `constants.py`.
   - Ensure the `NEWS_API_KEY` is obtained from the [News API](https://newsapi.org/) website.
   - Add the sender email address under `SENDER_EMAIL` in `constants.py`.
   - Add the sender email password under `SENDER_PASSWORD`.
   - When prompted, enter the receiver email address.
5. Execute the script in the command line interface (CLI) with two arguments for topic and language using the following command: `python main.py tesla en`

## Usage
1. Run the script using `python main.py`, or provide two arguments for topic and language like `python main.py tesla en`, or simply specify the topic as a single argument like `python main.py tesla` (default language is specified in this case).
2. Enter the topic you want to get news about when prompted.
3. Enter the language code in ISO format (e.g., 'en' for English) when prompted.
4. Check your email for the latest news articles.

## Contributing
Contributions are welcome! Here are some ways you can contribute to the project:
- Report bugs and issues
- Suggest new features or improvements
- Submit pull requests with bug fixes or enhancements

## Author
- Emad &nbsp; E>
  
  [<img src="https://img.shields.io/badge/GitHub-Profile-blue?logo=github" width="150">](https://github.com/emads22)

## License
This project is licensed under the MIT License, which grants permission for free use, modification, distribution, and sublicense of the code, provided that the copyright notice (attributed to [emads22](https://github.com/emads22)) and permission notice are included in all copies or substantial portions of the software. This license is permissive and allows users to utilize the code for both commercial and non-commercial purposes.

Please see the [LICENSE](LICENSE) file for more details.

