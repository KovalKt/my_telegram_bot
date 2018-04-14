# import requests
# import datetime
# from time import sleep
from config import BOT_TOKEN


# class BotHandler:

#     def __init__(self, token):
#         self.token = token
#         self.api_url = "https://api.telegram.org/bot{}/".format(token)

#     def get_updates(self, offset=None, timeout=60):
#         method = 'getUpdates'
#         params = {'timeout': timeout, 'offset': offset}
#         resp = requests.get(self.api_url + method, params)
#         result_json = resp.json()['result']
#         return result_json

#     def send_message(self, chat_id, text):
#         params = {'chat_id': chat_id, 'text': text}
#         print(params)
#         method = 'sendMessage'
#         resp = requests.post(self.api_url + method, params)
#         print("response after message sent", resp)
#         return resp

#     def get_last_update(self):
#         get_result = self.get_updates()

#         if len(get_result) > 0:
#             last_update = get_result[-1]
#         else:
#             last_update = []

#         return last_update


# greet_bot = BotHandler(BOT_TOKEN)  
# greetings = ('здравствуй', 'привет', 'ку', 'здорово')  
# now = datetime.datetime.now()


# def main():  
#     new_offset = None
#     today = now.day
#     hour = now.hour

#     while True:
#         greet_bot.get_updates(new_offset)

#         last_update = greet_bot.get_last_update()
        
#         if not last_update:
#             continue

#         last_update_id = last_update['update_id']
#         last_chat_text = last_update['message']['text']
#         last_chat_id = last_update['message']['chat']['id']
#         last_chat_name = last_update['message']['chat']['first_name']

#         if last_chat_text.lower() in greetings and today == now.day and 6 <= hour < 12:
#             greet_bot.send_message(last_chat_id, 'Доброе утро, {}'.format(last_chat_name))
#             today += 1

#         elif last_chat_text.lower() in greetings and today == now.day and 12 <= hour < 17:
#             greet_bot.send_message(last_chat_id, 'Добрый день, {}'.format(last_chat_name))
#             today += 1

#         elif last_chat_text.lower() in greetings and today == now.day and 17 <= hour <= 23:
#             greet_bot.send_message(last_chat_id, 'Добрый вечер, {}'.format(last_chat_name))
#             today += 1

#         new_offset = last_update_id + 1

# if __name__ == '__main__':  
#     try:
#         main()
#     except KeyboardInterrupt:
#         exit()


import os
from telegram.ext import Updater, CommandHandler
from quotes import get_random_quote

# Your bot token (from BotFather)
token = BOT_TOKEN
PORT = int(os.environ.get('PORT', '8443'))

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=("Hi %s. Send me /quote command to get a random quote from "
                                                          "me!" %
                                                          update.message.from_user.name))

def quote(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text=get_random_quote())

def main():
    updater = Updater(token);
    dp = updater.dispatcher

    # Define all the commands that the bot will receive
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("quote", quote))

    # # Start the bot
    # updater.start_polling()
    # print("================================")
    # print("========= Bot Running ==========")
    # print("================================")

    # add handlers
    updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=token)
    updater.bot.set_webhook("https://aqueous-ridge-88309.herokuapp.com/" + token)

    updater.idle()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
