#!/usr/bin/env python3

import sys
import logging
import argparse

import telebot
#from telebot import apihelper


#apihelper.proxy = {'https':'socks5://127.0.0.1:9050'}

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--debug', action='store_const', const=True, help = 'Set logging level "DEBUG"')
    parser.add_argument('-i', '--info', action='store_const', const=True, help = 'Set logging level "INFO"')
    parser.add_argument('-w', '--warning', action='store_const', const=True, help = 'Set logging level "WARNING"')
    parser.add_argument('-e', '--error', action='store_const', const=True, help = 'Set logging level "ERROR"')
    parser.add_argument('-c', '--critical', action='store_const', const=True, help = 'Set logging level "CRITICAL"')
    return parser

token = input('Enter token: ')
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['getid'])
def get_chat_id(message):
    bot.send_message(message.chat.id, message.chat.id)

@bot.channel_post_handler(commands=['getid'])
def get_channel_id(message):
    bot.send_message(message.chat.id, message.chat.id)

def main(use_logging=False, level_name=None):
    if use_logging:
        logging.basicConfig(format='%(levelname)-8s [%(asctime)s] %(message)s', filename='/tmp/get_telegram_id.log')
        telebot.logger.setLevel(logging.getLevelName(level_name))
        bot.polling()
    else:
        bot.polling()

if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    if namespace.debug is True:
        main(True, 'DEBUG')
        sys.exit()
    elif namespace.info is True:
        main(True, 'INFO')
        sys.exit()
    elif namespace.warning is True:
        main(True, 'WARNING')
        sys.exit()
    elif namespace.error is True:
        main(True, 'ERROR')
        sys.exit()
    elif namespace.critical is True:
        main(True, 'CRITICAL')
        sys.exit()
    else:
        main()
