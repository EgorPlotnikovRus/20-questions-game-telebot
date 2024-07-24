from dotenv import load_dotenv
import os

import telebot
from telebot import types

import logic
import texts

load_dotenv("config.env")

bot = telebot.TeleBot(os.getenv('TELEGRAM_TOKEN'))

game = logic.Game()

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Начать")
    markup.add(item1)
    bot.send_message(message.chat.id, texts.start_message, reply_markup=markup)
    bot.register_next_step_handler(message, on_begin_click)

def on_begin_click(message):
    if message.text == "Начать":
        play(message)
    else:
        start(message)
@bot.message_handler(commands=['play'])
def play(message):
    global game
    game = logic.Game()

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Закончить")
    markup.add(item1)
    bot.send_message(message.chat.id, texts.play_message, reply_markup=markup)
    bot.register_next_step_handler(message, on_finish_click)

def on_finish_click(message):
    if message.text == "Закончить":
        start(message)

    else:
        text_procesing(message)
@bot.message_handler()
def text_procesing(message):



bot.polling(non_stop=True)