
import sys
import os

# Add root folder to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from simplai.wishper_client import WhisperClient
from simplai.wishper_client import Verbosity


if __name__ == "__main__":

    audio_path = "examples/audio/audio_example.m4a"
    lang = "es"

    try:
        print("Creating object WishperClient...")
        client = WhisperClient(language=lang, verbosity=Verbosity.QUIET)
        print(f"Transcribe text from file: '{audio_path}' in language:{lang}")
        text = client.transcribe_from_audio_file(audio_path)
        print(f"Transcribed text:\n[START]:\n{text}\n[FINISHED]")

    except Exception as e:
        print(f"Error ocurred: {e}")
