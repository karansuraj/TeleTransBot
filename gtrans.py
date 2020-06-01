import flask
import json
import os
import telebot
from flask import request, jsonify
from translate import detect_language, translate_text

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.errorhandler(404)
def page_not_found(e):
    """ Used to handle 404 errors """
    print(e)
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/', methods=['GET'])
def home():
    """ Home page """
    return '''<h1>Google Translate Bot</h1>
<p>An API translating non-english sentences to English ones for a Telegram bot.</p>'''

@app.route('/detect', methods=['GET'])
def detectLanguage():
    """ REST API call to detect language of text """
    query_parameters = request.args
    text = query_parameters.get('text')
    if not text:
        return ""
    result = detect_language(text)
    return result


@app.route('/translate', methods=['GET'])
def translate():
    """ REST API call to translate whatever language text to English """
    query_parameters = request.args
    text = query_parameters.get('text')
    if not text:
        return ''
    translated = translate_text('en',text)
    if not translated:
        return ''
    return translated


if __name__ == '__main__':
    # Start flask app
    app.run()

    # Start Telegram bot polling agent
    telebot.poll_bot()
