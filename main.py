from telegram.ext import Updater, Dispatcher, CommandHandler, CallbackContext
from telegram.update import Update
import wikipedia
import requests
import settings

updater = Updater(token=settings.TELEGRAM_TOKEN)

wikipedia.set_lang('uz')


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Assalomu alaykum! Wikipediadan izlamoqchi bo‘lgan maqolani izlash uchun "
                              "/search ___(Kalit so‘z) kiriting. Agarda xato kiritilgan bo‘lsa maqola "
                              "topilmaydi")

def search(update: Update, context: CallbackContext):
    args = context.args
    if len(args) == 0:
        update.message.reply_text("Iltimos biror bir kalit so`z kiriting")
    else:
        try:
            search_text = ' '.join(args)
            summary_ = wikipedia.summary(search_text)
            r = requests.get("https://uz.wikipedia.org/w/api.php", {
                'action': "opensearch",
                'search': search_text,
                'limit': 1,
                'namespace': 0,
                'format': 'json'
            })
            res = r.json()
            link = res[3]
            update.message.reply_text(f"{summary_}\nBatafsil: {link[0]}")
        except:
            update.message.reply_text("Hech qanday maqola topilmadi")

dispatcher: Dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('search', search))

if __name__ == '__main__':
    updater.start_polling()
    updater.idle()
