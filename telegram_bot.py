import telebot
from telebot import apihelper
import os
import random

#apihelper.proxy = {'http':'http://10.10.1.10:3128'}

bot = telebot.TeleBot("API")

@bot.message_handler(commands = ['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Type /c_list for command list')

@bot.message_handler(commands = ['c_list'])
def send_help(message):
    bot.send_message(message.chat.id, '/pic - send random anime picture\n/for_klim - send picture of Klim\n/gif - send random gif')

@bot.message_handler(commands = ['for_klim'])
def send_klim(message):
    bot.send_message(message.chat.id, 'Wait a sec')
    pic = open('/Users/79771/Desktop/tbot/img/klim.jpg', 'rb')
    bot.send_photo(message.chat.id, pic)
    pic.close()

@bot.message_handler(commands = ['pic'])
def send_pic(message):
    bot.send_message(message.chat.id, 'Wait a sec')
    pic_path = os.chdir(r'/Users/79771/Desktop/tbot/img')
    pic = open(random.choice(os.listdir(pic_path)), 'rb')
    bot.send_photo(message.chat.id, pic)
    pic.close()

@bot.message_handler(commands = ['gif'])
def send_gif(message):
    bot.send_message(message.chat.id, 'Wait a sec')
    pic_path = os.chdir(r'/Users/79771/Desktop/tbot/gif')
    pic = open(random.choice(os.listdir(pic_path)), 'rb')
    bot.send_animation(message.chat.id, pic)
    pic.close()

bot.polling(none_stop = True, timeout = 100000)
