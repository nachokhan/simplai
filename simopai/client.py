from openai import OpenAI
from exceptions import OpenAIKeyException


class Client():
    def __init__(self, openai_key) -> None:
        self.client = None

        self._create_open_ai_client(openai_key)

    def _create_open_ai_client(self, key) -> None:
        if not key:
            raise OpenAIKeyException(message="No OpenAI key provided")

        if not isinstance(key, str):
            raise OpenAIKeyException(message="OpenAI key must be a sting")

        self.client = OpenAI(api_key=key)
