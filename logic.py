from  openai_helpers import  Client
import texts
from Levenshtein import distance as lev
import random

class Game:
    def __init__(self):
        self.current_question = 0
        self.item = texts.items[random.randint(0, len(texts.items) - 1)]
        self.client = Client(self.item)
        self.last_question = None
        self.last_question_answer = None

    def ask_question(self, question):
# todo: question len limit
        self.last_question = question
        self.current_question += 1
        self.client.ask_question(question)
        self.last_question_answer = self.client.give_answer()
    def get_answer(self):
        return self.last_question_answer

    def get_item(self):
        return self.item

    def is_game_over(self):
        return self.current_question >= 20

    def is_correct_answer(self):
        lev_dist = [lev(self.get_item().lower(), word.lower()) for word in self.last_question.split()]
        return True if min(lev_dist) < 3 else False

