from dotenv import load_dotenv
import os
import telebot
from telebot import types
import logic
import constants

load_dotenv("config.env")

bot = telebot.TeleBot(os.getenv('TELEGRAM_TOKEN'))

def create_keyboard(buttons: list[str]) -> types.ReplyKeyboardMarkup:
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for button in buttons:
        markup.add(types.KeyboardButton(button))
    return markup

@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message) -> None:
    bot.send_message(message.chat.id, constants.START_MESSAGE, reply_markup=create_keyboard([constants.START_BUTTON]))
    bot.register_next_step_handler(message, on_begin_click)

def on_begin_click(message: telebot.types.Message) -> None:
    if message.text == constants.START_BUTTON:
        play(message)
    else:
        wait_for_new_game(message)

@bot.message_handler(commands=['play'])
def play(message: telebot.types.Message) -> None:
    game = logic.Game()

    bot.send_message(message.chat.id, constants.PLAY_MESSAGE, reply_markup=create_keyboard([constants.FINISH_BUTTON]))
    bot.register_next_step_handler(message, on_finish_click, game)

def on_finish_click(message: telebot.types.Message, game: logic.Game) -> None:
    if message.text == constants.FINISH_BUTTON:
        wait_for_new_game(message)
    else:
        text_procesing(message, game)

def wait_for_new_game(message: telebot.types.Message) -> None:
    bot.send_message(message.chat.id, constants.WAIT_MESSAGE, reply_markup=create_keyboard([constants.START_BUTTON]))
    bot.register_next_step_handler(message, on_begin_click)

@bot.message_handler()
def text_procesing(message: telebot.types.Message, game: logic.Game) -> None:
    try:
        game.ask_question(message.text)
    except AttributeError:
        wait_for_new_game(message)

    handle_game_state(message, game)

def handle_game_state(message: telebot.types.Message, game: logic.Game) -> None:
    if game.is_correct_answer():
        bot.send_message(message.chat.id, constants.GAME_WIN_TEXT.format(game.get_item()))
        wait_for_new_game(message)
    elif game.is_game_over():
        bot.send_message(message.chat.id, constants.GAME_OVER_TEXT.format(game.get_item()))
        wait_for_new_game(message)
    else:
        bot.send_message(message.chat.id, game.get_answer(), reply_markup=create_keyboard([constants.FINISH_BUTTON]))
        bot.register_next_step_handler(message, on_finish_click, game)

if __name__ == '__main__':
    bot.polling(non_stop=True)