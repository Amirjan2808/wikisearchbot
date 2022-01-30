from telegram.ext import Updater, Dispatcher, CommandHandler, CallbackContext
from telegram.update import Update
import settings

updater = Updater(token=settings.TELEGRAM_TOKEN)

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Salom!")

dispatcher: Dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))

if __name__ == '__main__':
    updater.start_polling()
    updater.idle()