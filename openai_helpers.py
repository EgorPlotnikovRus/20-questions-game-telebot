from dotenv import load_dotenv
import os

from openai import OpenAI

import texts

load_dotenv("config.env")

class Client:
    def __init__(self, item):
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'), base_url='https://bothub.chat/api/v2/openai/v1')
        self.item = item
        self.context = texts.context(self.item)
        self.messages = []
        self.answers = []

    def ask_question(self, question):
        self.messages.append(question)
        self.answers.append(self.client.chat.completions.create(model="gpt-4o-mini", messages=[{"role": "user", "content": self.context + question}]).choices[0].message.content)

    def give_answer(self):
        return self.answers[-1]