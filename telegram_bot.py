import telebot
import os
import random

bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands = ['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Type /c_list for command list')

@bot.message_handler(commands = ['c_list'])
def send_help(message):
    bot.send_message(message.chat.id, '/pic - send random anime picture\n/for_klim - send picture of Klim\n/gif - send random gif')

@bot.message_handler(commands = ['for_klim'])
def send_klim(message):
    bot.send_message(message.chat.id, 'Wait a sec')
    pic = open('PATH', 'rb')
    bot.send_photo(message.chat.id, pic)
    pic.close()

@bot.message_handler(commands = ['pic'])
def send_pic(message):
    bot.send_message(message.chat.id, 'Wait a sec')
    pic_path = os.chdir(r'PATH')
    pic = open(random.choice(os.listdir(pic_path)), 'rb')
    bot.send_photo(message.chat.id, pic)
    pic.close()

@bot.message_handler(commands = ['gif'])
def send_gif(message):
    bot.send_message(message.chat.id, 'Wait a sec')
    pic_path = os.chdir(r'PATH')
    pic = open(random.choice(os.listdir(pic_path)), 'rb')
    bot.send_animation(message.chat.id, pic)
    pic.close()

bot.polling(none_stop = True, timeout = 100000)
