import telebot
import schedule
import time
import config
import os

API_TOKEN = os.environ.get('TELEGRAM_BOT_API_TOKEN')
bot = telebot.TeleBot(API_TOKEN, parse_mode = 'MarkDown');

print(time.ctime())

# @bot.message_handler()
# def send_message(message):
#     if message.chat.id == config.test_group_id:
#         send_message = bot.send_message(message.chat.id, message.text)
#         bot.unpin_chat_message(message.chat.id, config.pin_message_id)
#         bot.pin_chat_message(message.chat.id, send_message.id, disable_notification = True)
#         config.pin_message_id = send_message.id

TARGET_GROUP = config.math_group_id
# TARGET_GROUP = config.test_group_id

def send_link(link, password = ''):
    print(time.ctime())
    send_message = bot.send_message(TARGET_GROUP, link)
    bot.unpin_chat_message(TARGET_GROUP, config.pin_message_id)
    bot.pin_chat_message(TARGET_GROUP, send_message.id, disable_notification = True)
    config.pin_message_id = send_message.id

    if password:
        bot.send_message(TARGET_GROUP, password)

# Monday
schedule.every().monday.at(config.second_time).do(send_link, link = config.informatics)
schedule.every().monday.at(config.thirth_time).do(send_link, link = config.mathematics)
schedule.every().monday.at(config.fourth_time).do(send_link, link = config.algebra)

# Tuesday
schedule.every().tuesday.at(config.second_time).do(send_link, link = config.discrete_math)
schedule.every().tuesday.at(config.thirth_time).do(send_link, link = config.discrete_math)
schedule.every().tuesday.at(config.fourth_time).do(send_link, link = config.english)

# Wednesday
# schedule.every().wednesday.at(config.second_time).do(send_link, link = config.foreign_literature)
schedule.every().wednesday.at(config.thirth_time).do(send_link, link = config.history)
schedule.every().wednesday.at(config.fourth_time).do(send_link, link = config.protection_of_ukraine, password = config.protection_of_ukraine_password)

# Thursday
schedule.every().thursday.at(config.second_time).do(send_link, link = config.physical_education)
schedule.every().thursday.at(config.thirth_time).do(send_link, link = config.foreign_literature)
schedule.every().thursday.at(config.fourth_time).do(send_link, link = config.economic_theory)

# Friday
schedule.every().friday.at(config.second_time).do(send_link, link = config.chemistry)
schedule.every().friday.at(config.thirth_time).do(send_link, link = config.mathematics)
# schedule.every().friday.at(config.fourth_time).do(send_link, link = config.foreign_literature)

# schedule.every(2).seconds.do(send_link, link = config.protection_of_ukraine, password = config.protection_of_ukraine_password)

while True:
    schedule.run_pending()
    time.sleep(15)

# bot.infinity_polling()