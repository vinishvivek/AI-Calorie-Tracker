from __future__ import annotations

from openai import OpenAI
from config.settings import settings

class OpenAIClientFactory:
    @staticmethod
    def create() -> OpenAI:
        if not settings.openai_api_key:
            raise ValueError("OPENAI_API_KEY missing. Add it to your .env file.")

        return OpenAI(api_key=settings.openai_api_key)
