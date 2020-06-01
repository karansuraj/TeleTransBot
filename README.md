# Telegram Google Translate Bot

This Python application is deployed at https://gteletransbot.herokuapp.com/. It is a POC not intended for commercial use. All private tokens are expected to be queried from system environment variables. The application queries the Google Translate API by 2 avenues
* A Flask-based REST API
* A polling agent that receives messages from a Telegram bot and responds with english translations of those messages to the bot

Text sent to be translated by the Google Translate API will be translated from any language other than English, as long as that text is written in the script of that language accurately.

## Flask REST API
There are REST GET endpoints at 'detect' and 'translate' where you can enter text and get a JSON response back with the language detected only for the 'detect' request and a JSON response with the text translated into English for the 'translate' request.

Here are some sample requests and their responses:

**Translate Request**

      https://gteletransbot.herokuapp.com/translate?text=apfel


    {
      "detectedSourceLanguage": "de",
      "input": "apfel",
      "translatedText": "Apple"
    }

**Detect Language Request**

      https://gteletransbot.herokuapp.com/detect?text=apfel


      {
        "confidence": 0.98828125,
        "input": "apfel",
        "language": "de"
      }

## Telegram API
The Telegram API makes use of a private token specifically provided for our bot that will be used.

This bot can be used in the Telegram app at:

`@googTransBot`

The API will run at the same time the Flask server is started. When the API is run, it will poll for any messages sent by users of the Telegram bot. When a user sends a message to the bot, the Telegram API will make a request to the Google Translate API, clean the the HTML response returned, and if the detected language of the response is not in English, it will send a message to the user with the translated text.


## Environment Variables Stored

client_secret="{contents_of_google_cloud_private_token_file}"

GOOGLE_APPLICATION_CREDENTIALS="{path_to_google_cloud_private_token}"

TELEGRAM_TOKEN="{telegram_bot_private_token}"


## Resources Used
Google Translate API: https://cloud.google.com/translate/docs/basic/setup-basic

Telegram API: https://github.com/python-telegram-bot/python-telegram-bot
