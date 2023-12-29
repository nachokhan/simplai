from simplai.models.whisper.whisper_model import WhisperModel
from simplai.models.whisper.enums import ModelSize, TaskType, Temperature, BeamSize, Precision, Verbosity, AudioProcessing, ComputeType, LongFileStrategy


class WhisperClient:
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
        self.client = None
        self.set_options(
            model_size=model_size,
            task_type=task_type,
            temperature=temperature,
            beam_size=beam_size,
            precision=precision,
            verbosity=verbosity,
            audio_processing=audio_processing,
            compute_type=compute_type,
            language=language,
            best_of=best_of,
            without_timestamps=without_timestamps,
            long_file_strategy=long_file_strategy,
        )

    def set_options(self,
                    model_size=ModelSize.BASE,
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
        self.client = WhisperModel(
            model_size=model_size,
            task_type=task_type,
            temperature=temperature,
            beam_size=beam_size,
            precision=precision,
            verbosity=verbosity,
            audio_processing=audio_processing,
            compute_type=compute_type,
            language=language,
            best_of=best_of,
            without_timestamps=without_timestamps,
            long_file_strategy=long_file_strategy,
        )

    def transcribe_from_audio_file(self, file: str) -> str:
        text = self.client.transcribe(file)
        return text
