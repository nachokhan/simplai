import pytest
from simplai.models.whisper.whisper_model import WhisperModel
from simplai.models.whisper.enums import ModelSize, TaskType, AudioProcessing, LongFileStrategy


# Define the path to the test audio file
TEST_AUDIO_FILE = "tests/models/whisper/audio/TEST.m4a"


# Create a WhisperModel instance for testing
@pytest.fixture
def whisper_model():
    model = WhisperModel(
        model_size=ModelSize.BASE,
        task_type=TaskType.TRANSCRIBE,
        audio_processing=AudioProcessing.NONE,
        long_file_strategy=LongFileStrategy.DEFAULT,
    )
    return model


def test_transcribe(whisper_model):
    transcription = whisper_model.transcribe(TEST_AUDIO_FILE)
    expected_transcription = "Hello, this is a simple test to test the testing functionalities. Number 2"
    assert transcription.strip() == expected_transcription.strip()


if __name__ == "__main__":
    pytest.main([__file__])
