import sys
import os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

import pytest
from simplai.client import Client


valid_api_key = 'your_valid_api_key'


def test_client_initialization_with_valid_key():
    client = Client(openai_key=valid_api_key)
    assert client.openai_client is not None


def test_client_initialization_with_no_key():
    with pytest.raises(Exception):
        client = Client(openai_key=None)


def test_client_initialization_with_non_string_key():
    with pytest.raises(Exception):
        client = Client(openai_key=123)


def test_client_initialization_print(capsys):
    client = Client(openai_key=valid_api_key)
    captured = capsys.readouterr()
    assert captured.out.strip() == str(client.openai_client)


if __name__ == '__main__':
    pytest.main()
