from google.cloud import dialogflow
import telebot
import config
import os

API_TOKEN = os.environ.get('TELEGRAM_BOT_API_TOKEN')
bot = telebot.TeleBot(API_TOKEN, parse_mode = 'MarkDown')

def detect_intent_texts(text, project_id = 's002-nwpa', session_id = 'session003', language_code = 'ru'):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    text_input = dialogflow.TextInput(text = text, language_code = language_code)
    query_input = dialogflow.QueryInput(text = text_input)
    response = session_client.detect_intent(request = {"session": session, "query_input": query_input})
    return response.query_result.fulfillment_text

@bot.message_handler(commands = ['start'])
def send_hi(message):
    if message.chat.type == 'private' or message.chat.type == 'group' or message.chat.type == 'supergroup':
        response = detect_intent_texts('привет')
        bot.send_message(message.chat.id, response)

@bot.message_handler()
def send_message(message):
    message.text = message.text.lower()
    find1 = '/002 '

    if message.chat.type == 'private':
        response = detect_intent_texts(message.text)
        if response:
            bot.send_message(message.chat.id, response)

    else:
        if message.text == find1.lstrip().rstrip():
            response = detect_intent_texts('привет')
            bot.send_message(message.chat.id, response)

        elif message.text.find(find1) == 0:
            response = detect_intent_texts(message.text[len(find1):])
            if response:
                bot.send_message(message.chat.id, response)

bot.infinity_polling()