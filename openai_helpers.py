from dotenv import load_dotenv
import os
import random

from openai import OpenAI

import texts

load_dotenv("config.env")

class Client:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'), base_url='https://bothub.chat/api/v2/openai/v1')
        self.item = texts.items[random.randint(0, len(texts.items)-1)]
        self.context = texts.context(self.item)
        self.messages = []
        self.answers = []
    def ask_question(self, question):
        self.messages.append(question)
        self.answers.append(self.client.chat.completions.create(model="gpt-4o-mini", messages=[{"role": "user", "content": self.context + question}]).choices[0].message.content)

    def give_answer(self):
        return self.answers[-1]

client = Client()

client.ask_question("Оно круглое?")
print(client.give_answer())
