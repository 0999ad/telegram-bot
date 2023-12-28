# Telegram Dark Web Link Finder Bot

This Telegram bot is designed to assist users in finding links to the dark web. It's a Python-based bot that uses the `telebot` library for its operations.

## Setup and Operation

Before using the bot, you need to obtain a Telegram bot token. This token should be assigned to the `BOT_TOKEN` variable in the script.

Once the bot is set up with the token and the script is running, it becomes operational on Telegram.

## Bot Commands

The bot recognizes two main commands:

1. **Start Command**: Users can initiate interaction with the bot by sending `/start` or `/hello`. The bot responds with a welcome message and basic instructions.

2. **Dark Web Search Command**: Users can search for dark web links by using the `/tor` or `/getonions` command followed by their query. For example, `/tor credit cards`. The bot will then provide relevant .onion links.

**Note**: Accessing these .onion links requires a TOR browser.

## Code Features

- **Bot Token**: The bot token is stored in the `BOT_TOKEN` variable.
- **Welcome Message Handler**: This function handles the `/start` and `/hello` commands, providing users with a welcome message and instructions.
- **Dark Web Search Handler**: This function processes the `/tor` and `/getonions` commands, performs a search based on the user's query, and returns .onion links.
- **Scraping Function**: The `scrape` function is responsible for fetching and processing .onion links from a specified URL based on the user's search query.
- **File Handling**: The bot saves the scraped links to a text file and reads the first few lines to send back to the user.

## Security Note

This bot interacts with dark web content, which can be sensitive and potentially illegal. 
Ensure you understand the risks and legal implications associated with such activities in your jurisdiction.

The original version was for an EC council course with Omar Rajab. 
