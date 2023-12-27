import whisper
from simopai.models.whisper.enums import ModelSize, TaskType, Temperature, BeamSize, AudioProcessing
from simopai.models.whisper.enums import Precision, ComputeType, Verbosity, LongFileStrategy
from simopai.models.whisper.preprocess_lib import preprocess_audio


class WhisperModel:
    def __init__(self, model_size=ModelSize.BASE,
                 task_type=TaskType.TRANSCRIBE,
                 temperature=Temperature.LOW,
                 beam_size=BeamSize.SMALL,
                 precision=Precision.FP32,
                 verbosity=Verbosity.QUIET,
                 audio_processing=AudioProcessing.NONE,
                 compute_type=ComputeType.AUTO,
                 language="en", best_of=None,
                 without_timestamps=False,
                 long_file_strategy=LongFileStrategy.DEFAULT):

        # Assign configurations from enumerations and parameters
        self.model_size = model_size
        self.task_type = task_type
        self.temperature = temperature.value
        self.beam_size = beam_size.value
        self.precision = precision
        self.verbosity = verbosity
        self.audio_processing = audio_processing
        self.compute_type = compute_type
        self.language = language
        self.best_of = best_of
        self.without_timestamps = without_timestamps
        self.long_file_strategy = long_file_strategy

        # Load the model with specified options
        self.model = whisper.load_model(
            self.model_size.value,
            # device=self.compute_type.name.lower()
        )

    def transcribe(self, audio_path):
        # Transcription options based on class configuration
        options = {
            "language": self.language,
            "task": self.task_type.value,
            "temperature": self.temperature,
            "beam_size": self.beam_size,
            "best_of": self.best_of,
            "without_timestamps": self.without_timestamps,
            # "log_probs": None,  # Specify if needed
            # "num_beams": None,  # Specify if needed
            "fp16": self.precision == Precision.FP16,  # Assuming Precision enum is used
            "suppress_tokens": None  # Specify if needed
        }

        # Pre process audio
        processed_audio_paths = preprocess_audio(
            audio_path,
            self.audio_processing,
            self.long_file_strategy,
        )

        # Initialize a list to store the transcription results for each processed segment
        transcription_results = []

        # Perform transcription for each processed audio segment
        for segment_path in processed_audio_paths:
            result = self.model.transcribe(segment_path, **options)
            transcription_results.append(result["text"])

        # Concatenate the transcription results from all segments if needed
        final_transcription = ' '.join(transcription_results)  # Modify as needed

        # Return the final transcription result
        return final_transcription
