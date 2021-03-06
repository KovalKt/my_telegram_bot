 # -*- coding: utf-8 -*-
import os
from config import BOT_TOKEN
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
    print("let's send quote")
    bot.sendMessage(chat_id=update.message.chat_id,
                    text=get_random_quote())

def main():
    updater = Updater(token);
    dp = updater.dispatcher

    # Define all the commands that the bot will receive
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("quote", quote))

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
