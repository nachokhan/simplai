import pytest
import sys
import os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from simopai.models.whisper.preprocess_lib import preprocess_audio
from simopai.models.whisper.enums import AudioProcessing, LongFileStrategy


TEST_AUDIO_FILE = "tests/models/whisper/audio/TEST.m4a"
TEST_LONG_AUDIO_FILE = "tests/models/whisper/audio/LONG_TEST.m4a"


# Test case 1: Normalization
def test_normalize_audio():
    processed_paths = preprocess_audio(TEST_AUDIO_FILE, AudioProcessing.NORMALIZE)

    assert len(processed_paths) == 1
    assert os.path.exists(processed_paths[0])


# Test case 2: Noise reduction
def test_reduce_noise():
    processed_paths = preprocess_audio(TEST_AUDIO_FILE, AudioProcessing.NOISE_REDUCTION)

    assert len(processed_paths) == 1
    assert os.path.exists(processed_paths[0])


# Test case 3: Splitting long audio
def test_split_long_audio():
    processed_paths = preprocess_audio(TEST_LONG_AUDIO_FILE, AudioProcessing.NORMALIZE, LongFileStrategy.SPLIT)

    assert len(processed_paths) > 1
    assert all(os.path.exists(path) for path in processed_paths)


# Test case 4: Windowing long audio
def test_window_long_audio():
    processed_paths = preprocess_audio(TEST_LONG_AUDIO_FILE, AudioProcessing.NORMALIZE, LongFileStrategy.WINDOW)

    assert len(processed_paths) > 1
    assert all(os.path.exists(path) for path in processed_paths)


# Test case 5: Default strategy with long audio
def test_default_long_audio():
    processed_paths = preprocess_audio(TEST_AUDIO_FILE, AudioProcessing.NORMALIZE)

    assert len(processed_paths) == 1
    assert os.path.exists(processed_paths[0])


# Test case 6: Invalid audio path
def test_invalid_audio_path():
    audio_path = 'non_existent_audio_file.wav'
    with pytest.raises(FileNotFoundError):
        preprocess_audio(audio_path, AudioProcessing.NORMALIZE)


# Test case 7: Unsupported processing type
def test_unsupported_processing_type():
    with pytest.raises(ValueError):
        preprocess_audio(TEST_AUDIO_FILE, 'invalid_processing_type')


# Test case 8: Invalid long file strategy
def test_invalid_long_file_strategy():
    with pytest.raises(ValueError):
        preprocess_audio(TEST_AUDIO_FILE, AudioProcessing.NORMALIZE, 'invalid_strategy')


# Test case 9: No processing
def test_no_processing():
    processed_paths = preprocess_audio(TEST_AUDIO_FILE, AudioProcessing.NONE)

    assert len(processed_paths) == 1
    assert os.path.exists(processed_paths[0])


# Test case 10: No long file strategy
def test_no_long_file_strategy():
    processed_paths = preprocess_audio(TEST_AUDIO_FILE, AudioProcessing.NORMALIZE, LongFileStrategy.DEFAULT)

    assert len(processed_paths) == 1
    assert os.path.exists(processed_paths[0])
