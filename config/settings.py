import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    """Store environment-driven configuration for models, tokens, and API access."""

    openai_api_key: str | None = os.environ.get("OPENAI_API_KEY")
    vision_model: str = os.environ.get("VISION_MODEL", "gpt-5.4-mini")
    max_tokens: int | None = int(os.environ.get("MAX_TOKENS", "800"))


settings = Settings()
