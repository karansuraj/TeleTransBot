import os
import html
import logging

from translate import detect_language, translate_text
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Can delete webhook if updates errors, using the following HTML request
# https://api.telegram.org/bot<token>/deleteWebhook

# Set up initial telegram updater and dispatcher and logging configs

# import json
# with open('secrets.json', 'r') as f:
#     parsed_json = json.load(f)
# telebotToken = parsed_json['telebotToken']
telebotToken = os.environ.get('TELEGRAM_TOKEN')

updater = Updater(token=telebotToken, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


def start(update, context):
    # Send welcome message to user when start command is invoked
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to the Google Translate bot! Any non-english text you type will be replied back to you in English.")


def echo(update, context):
    # Translate the incoming message text and unescape any escaped HTML characters
    translatedObject = translate_text('en',update.message.text)
    translatedText = translatedObject['translatedText']
    cleanedText = html.unescape(translatedText)

    # If the original message was not in English, send the translated response to the user
    if translatedObject['detectedSourceLanguage'] != 'en':
        context.bot.send_message(chat_id=update.effective_chat.id, text=cleanedText)

# Adding a handler for the start command from the user
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Adding a handler for general messages from user
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

def poll_bot():
    # Get the telegram bot polling
    updater.start_polling()

if __name__ == '__main__':
    poll_bot()
