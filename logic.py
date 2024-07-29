from typing import Optional
from  openai_helpers import  Client
import constants
from Levenshtein import distance as lev
import random

class Game:
    def __init__(self) -> None:
        self.current_question = 0
        self.item = random.choice(constants.ITEMS)
        self.client = Client(self.item)
        self.last_question = ""
        self.last_question_answer = None

    def ask_question(self, question: str) -> None:
        if len(question) > 100:
            self.last_question_answer = constants.ERROR_LEN_QUEST
            return

        self.last_question = question
        self.current_question += 1
        self.last_question_answer = self.client.ask_question(question)

        if self.last_question_answer not in ['Да.', 'Нет.']:
            self.last_question_answer = constants.ASK_ANOTHER_QUESTION

    def get_answer(self) -> Optional[str]:
        return self.last_question_answer

    def get_item(self) -> str:
        return self.item

    def is_game_over(self) -> bool:
        return self.current_question >= 20

    def is_correct_answer(self) -> bool:
        if self.last_question_answer is None:
            return False

        lev_dist = [lev(self.get_item().lower(), ''.join(w for w in word if w.isalpha()).lower()) for word in self.last_question.split()]
        return min(lev_dist) < 3