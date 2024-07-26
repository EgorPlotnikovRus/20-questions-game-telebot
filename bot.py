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
        wait(message)

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
        wait(message)

    else:
        text_procesing(message)

def wait(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Начать")
    markup.add(item1)
    bot.send_message(message.chat.id, texts.wait_message, reply_markup=markup)
    bot.register_next_step_handler(message, on_begin_click)

@bot.message_handler()
def text_procesing(message):
    game.ask_question(message.text)

    if game.is_correct_answer():
        game_win_state(message)

    elif game.is_game_over():
        game_over_state(message)

    else:
        #bot.send_message(message.chat.id, game.get_answer())
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Закончить")
        markup.add(item1)
        bot.send_message(message.chat.id, game.get_answer(), reply_markup=markup)
        bot.register_next_step_handler(message, on_finish_click)

def game_over_state(message):
    bot.send_message(message.chat.id, texts.game_over_text(game.get_item()))
    wait(message)

def game_win_state(message):
    bot.send_message(message.chat.id, texts.game_win_text(game.get_item()))
    wait(message)

if __name__ == '__main__':
    bot.polling(non_stop=True)