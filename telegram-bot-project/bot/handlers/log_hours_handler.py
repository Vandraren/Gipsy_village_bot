from telegram import Update
from telegram.ext import CallbackContext

def log_hours(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    message = update.message.text

    # Here you would process the message to log hours
    # For example, you might extract the hours from the message
    # and then call a service to save it to an Excel file.

    # Notify the user that their hours have been logged
    context.bot.send_message(chat_id=user_id, text="Your working hours have been logged successfully!")