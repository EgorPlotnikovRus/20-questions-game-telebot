class Game:
    def __init__(self):
        self.current_question = 0

    def ask_question(self, question):
        self.current_question += 1

    def give_answer(self, answer):
        pass
    def is_game_over(self):
        return self.current_question >= 20
