import os
import librosa
import noisereduce as nr
import soundfile as sf
from simopai.models.whisper.enums import AudioProcessing
from simopai.models.whisper.enums import LongFileStrategy


def preprocess_audio(audio_path, processing_type=AudioProcessing.NONE, long_file_strategy=LongFileStrategy.DEFAULT):
    """
    Preprocess an audio file.

    Args:
        audio_path (str): Path to the audio file.
        processing_type (AudioProcessing): The type of audio processing to apply.
        long_file_strategy (LongFileStrategy): The strategy to handle long audio files.

    Returns:
        List[str]: List of paths to the processed audio segments.
    """

    # Check the file exists
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"{audio_path} does not exist!")

    # Check the processing type exists and is valid
    if processing_type not in [at.value for at in AudioProcessing]:
        if not isinstance(processing_type, AudioProcessing):
            raise ValueError("Unsupported processing_type")

    # Check the long file strategy exists and is valid
    if long_file_strategy not in [at.value for at in LongFileStrategy]:
        if not isinstance(long_file_strategy, LongFileStrategy):
            raise ValueError("Unsupported long_file_strategy")

    # Load the audio file. sr=None retains the original sampling rate.
    audio, sr = librosa.load(audio_path, sr=None)

    # Apply processing based on the specified type
    if processing_type == AudioProcessing.NORMALIZE:
        # Apply normalization or gain adjustment
        audio = librosa.util.normalize(audio)

    if processing_type == AudioProcessing.NOISE_REDUCTION:
        # Apply noise reduction using noisereduce library
        # This assumes that the entire audio can be used as a noise profile
        # For better results, consider providing a specific noise profile from a segment of audio known to contain only noise.
        audio = nr.reduce_noise(y=audio, sr=sr)

    # Handle long audio files based on the specified strategy
    if long_file_strategy == LongFileStrategy.SPLIT:
        segments = _split_audio(audio, sr)
    elif long_file_strategy == LongFileStrategy.WINDOW:
        segments = _window_audio(audio, sr)
    else:
        segments = [audio]  # Default to using the whole audio as one segment

    # Process each segment and save to temporary files
    processed_audio_paths = []

    for i, segment in enumerate(segments):
        segment_path = _get_audio_path(audio_path, i)
        sf.write(segment_path, segment, sr, subtype='PCM_24')
        processed_audio_paths.append(segment_path)

    return processed_audio_paths


def _get_audio_path(audio_path, segment_number):
    audio_filename = os.path.splitext(os.path.basename(audio_path))[0]
    segment_path = os.path.join(
        os.path.dirname(audio_path),
        f"segment_{segment_number}_{audio_filename}.wav"
    )
    return segment_path


def _split_audio(audio, sr, segment_length_sec=10):
    """
    Split an audio signal into segments.

    Args:
        audio (numpy.ndarray): The input audio signal.
        sr (int): The sampling rate of the audio.
        segment_length_sec (int): The length of each segment in seconds.

    Returns:
        List[numpy.ndarray]: List of audio segments.
    """
    # Determine the segment length in samples
    segment_length = segment_length_sec * sr
    total_samples = len(audio)

    # Split the audio into segments
    segments = [audio[i:i+segment_length] for i in range(0, total_samples, segment_length)]
    return segments


def _window_audio(audio, sr, window_length_sec=10, overlap_sec=2):
    """
    Create overlapping windows from an audio signal.

    Args:
        audio (numpy.ndarray): The input audio signal.
        sr (int): The sampling rate of the audio.
        window_length_sec (int): The length of each window in seconds.
        overlap_sec (int): The overlap between consecutive windows in seconds.

    Returns:
        List[numpy.ndarray]: List of audio windows.
    """
    window_length = window_length_sec * sr
    overlap = overlap_sec * sr
    step_size = window_length - overlap
    total_samples = len(audio)

    # Create overlapping windows
    windows = [audio[i:i+window_length] for i in range(0, total_samples - overlap, step_size)]
    return windows
