from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

OpenAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai_client = OpenAI(api_key=OpenAI_API_KEY)