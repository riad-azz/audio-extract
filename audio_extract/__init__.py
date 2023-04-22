# Other modules
import os

# Local modules
from audio_extract import utils
from audio_extract import validators
from audio_extract import ffmpeg_tools
from audio_extract.exceptions import AudioExtractException


def extract_full_audio(input_path: str, output_path: str, start_time: str):
    if not validators.extract_full_audio_validation(input_path, start_time):
        return False
    ffmpeg_tools.extract_full_audio(input_path, output_path, start_time)
    return True


def extract_sub_audio(input_path: str, output_path: str, start_time: str, duration: str):
    if not validators.extract_sub_audio_validation(input_path, start_time, duration):
        return False
    ffmpeg_tools.extract_sub_audio(input_path, output_path, start_time, duration)
    return True


def run(input_path: str, output_path: str = "./audio.mp3", start_time: str = "00:00", duration: str | None = None):
    input_path = os.path.abspath(input_path)
    output_path = os.path.abspath(output_path)

    if not os.path.exists(input_path):
        utils.print_error(f"{input_path} does not exist")
        return False

    print(f"Processing audio for {input_path} please wait...")

    if not output_path.endswith(".mp3"):
        output_path += ".mp3"

    try:
        if not duration:
            return extract_full_audio(input_path, output_path, start_time)
        else:
            return extract_sub_audio(input_path, output_path, start_time, duration)
    except Exception as e:
        if isinstance(e, AudioExtractException):
            utils.print_error(e.message)
        else:
            utils.print_error(f"Something went wrong, {e}")
        return False
