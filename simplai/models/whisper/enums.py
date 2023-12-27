from enum import Enum, auto


# Enum for different model sizes available in Whisper
class ModelSize(Enum):
    TINY = "tiny"
    BASE = "base"
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"


# Enum for the type of task to perform (transcription or translation)
class TaskType(Enum):
    TRANSCRIBE = "transcribe"
    TRANSLATE = "translate"


# Enum for temperature settings affecting randomness in generation
class Temperature(Enum):
    LOW = 0.0
    MEDIUM = 0.7
    HIGH = 1.0


# Enum for beam size in decoding, affecting quality and compute time
class BeamSize(Enum):
    SMALL = 1
    MEDIUM = 5
    LARGE = 10


# Enum for precision type in computation (floating point)
class Precision(Enum):
    FP32 = "fp32"
    FP16 = "fp16"


# Enum for verbosity levels in logging and output
class Verbosity(Enum):
    QUIET = 0
    VERBOSE = 1


# Enum for types of audio processing to be applied before transcription
class AudioProcessing(Enum):
    NONE = auto()
    NORMALIZE = auto()
    NOISE_REDUCTION = auto()


# Enum for specifying the compute device type (CPU/GPU)
class ComputeType(Enum):
    AUTO = auto()
    GPU = auto()
    CPU = auto()


class LongFileStrategy(Enum):
    DEFAULT = 'default'  # Use the whole audio as one segment (default behavior)
    SPLIT = 'split'      # Split the audio into segments
    WINDOW = 'window'    # Create overlapping windows from the audio
