#!/usr/bin/env python3

import argparse
import logging
import sys

import telebot


__version__ = '0.1'

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=(
        'How to use:\n'
        ' * Create a bot.\n'
        ' * Get a token.\n'
        ' * Launch the bot and give it a token.\n'
        ' * To get the id of a chat with a bot send the /getid command to it.\n'
        ' * To get the channel id make the bot an administrator in that channel and then send '
        'the /getid command.\n'
        ' * To get the group id add the bot to the group and send the /getid command.\n'
        'After sending the command the bot will show the id in the terminal if you use the "info" '
        'or "debug" logging levels, and will also send the id to the chat if it has the rights to '
        'send messages')
)
group = parser.add_mutually_exclusive_group()
group.add_argument(
    '-i', '--info', action='store_true',
    help = 'set logging level "INFO"'
)
group.add_argument(
    '-d', '--debug', action='store_true',
    help = 'set logging level "DEBUG"'
)
group.add_argument(
    '-e', '--error', action='store_true',
    help = argparse.SUPPRESS
)
group.add_argument(
    '-w', '--warning', action='store_true',
    help = argparse.SUPPRESS
)
group.add_argument(
    '-c', '--critical', action='store_true',
    help = argparse.SUPPRESS
)
args = parser.parse_args()

token = input('Enter token: ')
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['getid'])
def get_chat_id(message):
    try:
        bot.send_message(message.chat.id, message.chat.id)
    except Exception as error:
        telebot.logger.error(error)
    telebot.logger.info(f'{message.chat.title} id: {message.chat.id}')

@bot.channel_post_handler(commands=['getid'])
def get_channel_id(message):
    try:
        bot.send_message(message.chat.id, message.chat.id)
    except Exception as error:
        telebot.logger.error(error)
    telebot.logger.info(f'{message.chat.title} id: {message.chat.id}')

def main(use_logging=False, level_name=None):
    if use_logging:
        logging.basicConfig(
            format='%(levelname)-8s [%(asctime)s] %(message)s',
            filename='/tmp/get_telegram_id.log'
        )
        telebot.logger.setLevel(logging.getLevelName(level_name))
        bot.polling()
    else:
        bot.polling()

if args.debug is True:
    main(True, 'DEBUG')
    sys.exit()
elif args.info is True:
    main(True, 'INFO')
    sys.exit()
elif args.warning is True:
    main(True, 'WARNING')
    sys.exit()
elif args.error is True:
    main(True, 'ERROR')
    sys.exit()
elif args.critical is True:
    main(True, 'CRITICAL')
    sys.exit()
else:
    main()
