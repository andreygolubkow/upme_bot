# -*- coding: utf-8 -*-
import config
import telebot
import time
from dic import *

def listener(messages):
    for m in messages:
        if m.content_type == 'text':
            bot.send_message(m.chat.id,onmessage(str(m.chat.id),m.text))

if __name__ == '__main__':
     bot = telebot.TeleBot(config.token)
     bot.set_update_listener(listener)
     bot.polling(none_stop=True)