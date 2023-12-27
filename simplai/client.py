from openai import OpenAI


class Client():
    def __init__(self, openai_key: str) -> None:
        self.openai_client = None

        self._create_open_ai_client(openai_key)

    def _create_open_ai_client(self, key) -> None:
        if not key:
            raise Exception("No OpenAI key provided")

        if not isinstance(key, str):
            raise Exception("OpenAI key must be a sting")

        self.openai_client = OpenAI(api_key=key)
        print(self.openai_client)


if __name__ == "__main__":
    client = Client(openai_key=123)
