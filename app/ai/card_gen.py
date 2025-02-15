import logging
import os
from pathlib import Path

import dotenv
from openai import OpenAI

from app.tools.open_file import open_file

logger = logging.getLogger(__name__)

class CardGen:
    system_prompt_path: Path = Path(__file__).parent.resolve() / "prompts"

    def __new__(cls, *args, **kwargs):
        dotenv.load_dotenv(os.path.join(os.path.dirname(__file__), "..", "..", ".env", ".env-chatgpt"))
        if os.getenv("OPEN_API_KEY") is None:
            raise ValueError("OPEN_API_KEY is not set in .env file")
        return super().__new__(cls)

    def __init__(self, model="gpt-3.5-turbo", response_format=None):
        self.response_format = response_format or {"type": "json_object"}
        self.client = OpenAI()
        self.model = model

    def process_flashcard(self, user_prompt: str):
        messages = [
            {"role": "system", "content": open_file(type(self).system_prompt_path / "system_prompt.txt")},
            {"role": "user", "content": user_prompt},
        ]

        logger.info(f"Creating card json for user: {len(user_prompt.split())}")
        self.client.chat.completions.create(
            model=self.model,
            response_format=self.response_format,
            messages=messages
        )
