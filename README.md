# 20 Questions Telegram Bot

This is a Telegram bot that plays the "20 Questions" game with users. The bot thinks of an item and the user asks yes/no questions to guess what the item is. The bot uses OpenAI's GPT model to understand and respond to the user's questions.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8+
- `pip` (Python package installer)
- A Telegram bot token (you can get one from [BotFather](https://core.telegram.org/bots#botfather))
- An OpenAI API key

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/EgorPlotnikovRus/20-questions-game-telebot.git
    cd 20-questions-game-telebot
    ```

2. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Create a `config.env` file in the project directory and add your Telegram bot token and OpenAI API key:
    ```sh
    TELEGRAM_TOKEN=your_telegram_bot_token
    OPENAI_API_KEY=your_openai_api_key
    ```

4. Run the bot:
    ```sh
    python bot.py
    ```

## Project Structure

```plaintext
20-questions-telegram-bot/
├── bot.py                # Main bot logic
├── logic.py              # Game logic
├── openai_helpers.py     # OpenAI client helper functions
├── constants.py          # Constants used throughout the project
├── requirements.txt      # Python package dependencies
├── config.env            # Environment variables (not included in the repo)
└── README.md             # This file
```

### bot.py

This file contains the main bot logic. It handles user interactions and manages the game state.

### logic.py

This file contains the game logic, including how questions are processed and how the game state is managed.

### openai_helpers.py

This file contains helper functions for interacting with the OpenAI API.

### constants.py

This file contains constants used throughout the project, such as messages and item lists.

## Usage

1. Start the bot by running `python bot.py`.
2. Open Telegram and find your bot.
3. Start a conversation with the bot by sending the `/start` command.
4. Follow the prompts to begin playing the game.
---