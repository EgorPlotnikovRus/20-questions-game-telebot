from typing import Optional
from dotenv import load_dotenv
import os
from openai import OpenAI
import constants

load_dotenv("config.env")

class Client:
    def __init__(self, item: str) -> None:
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'), base_url='https://bothub.chat/api/v2/openai/v1')
        self.context = constants.CONTEXT.format(item)

    def ask_question(self, question: str) -> Optional[str]:
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": self.context + question}]
            )
            answer = response.choices[0].message.content
            return answer
        except Exception as e:
            print(f"Error: {e}")
            return None