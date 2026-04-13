import os

from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
    openai_api_key  : str | None    = os.environ.get("OPENAI_API_KEY")
    vision_model    : str           = os.environ.get("VISION_MODEL", "gpt-4o-mini")
    max_tokens      : int | None    = int(os.environ.get("MAX_TOKENS", "300"))

settings = Settings()
