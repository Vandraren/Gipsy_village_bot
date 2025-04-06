from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from utils.config import TOKEN

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome! Please log your working hours.')

def log_hours(update: Update, context: CallbackContext) -> None:
    # Logic to log hours will be implemented in the handler
    update.message.reply_text('Please enter the hours you worked.')

def main() -> None:
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("log_hours", log_hours))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()