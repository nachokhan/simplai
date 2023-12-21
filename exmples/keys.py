from dotenv import load_dotenv
import os

config = load_dotenv("KEYS.env")
OPENAI_KEY = os.environ.get('OPENAI_KEY')
