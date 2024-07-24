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
    print

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Закончить")
    markup.add(item1)
    bot.send_message(message.chat.id, texts.play_message, reply_markup=markup)
    bot.register_next_step_handler(message, on_finish_click)
    print("bot/play ", game.__get_current_question__())

def on_finish_click(message):
    print("bot/on_finish_click ", game.__get_current_question__())
    if message.text == "Закончить":
        start(message)

    else:
        text_procesing(message)

@bot.message_handler()
def text_procesing(message):
    print("bot/text_procesing ", game.__get_current_question__())
    game.ask_question(message.text)

    if game.is_correct_answer():
        game_win_state(message)

    elif game.is_game_over():
        game_over_state(message)

    else:
        bot.send_message(message.chat.id, 'hui')
        bot.send_message(message.chat.id, game.get_answer())

def game_over_state(message):
    print("bot/game_over_state ", game.__get_current_question__())
    bot.send_message(message.chat.id, texts.game_over_text(game.get_item()))
    start(message)
def game_win_state(message):
    print("bot/game_win_state ", game.__get_current_question__())
    bot.send_message(message.chat.id, texts.game_win_text(game.get_item()))
    start(message)

bot.polling(non_stop=True)