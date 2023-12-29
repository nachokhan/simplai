
import sys
import os

# Agrega el directorio raíz del proyecto al sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from keys import OPENAI_KEY
from simplai.client import Client


PROMPT = "Translate this text to {dest_lang}: {text}"

client = Client(OPENAI_KEY)

lan = "german"
text = "Buenos dias! Estoy orgullosamente listo para triunfar hoy día"
prompt = prompt = PROMPT.format(dest_lang=lan, text=text)

print(prompt)
