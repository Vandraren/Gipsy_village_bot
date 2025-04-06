# Telegram Bot for Logging Working Hours

This project is a Telegram bot designed to notify users to log their working hours in Excel tables. It provides an easy-to-use interface for users to track their time and manage their work hours efficiently.

## Features

- Notifications to remind users to log their working hours.
- Integration with Excel for storing and managing logged hours.
- User-friendly commands for logging and retrieving work hours.

## Project Structure

```
telegram-bot-project
├── bot
│   ├── __init__.py
│   ├── main.py
│   ├── handlers
│   │   ├── __init__.py
│   │   └── log_hours_handler.py
│   ├── services
│   │   ├── __init__.py
│   │   └── excel_service.py
│   └── utils
│       ├── __init__.py
│       └── config.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd telegram-bot-project
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure your bot token and other settings in `bot/utils/config.py`.

## Usage

1. Run the bot:
   ```
   python bot/main.py
   ```

2. Interact with the bot on Telegram using the commands provided.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.