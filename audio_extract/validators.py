import os
import re
import magic
from audio_extract import utils
from audio_extract.exceptions import AudioExtractException


def is_valid_hms(time: str) -> bool:
    if type(time) is not str:
        return False
    # Pattern to match HH:MM:SS or MM:SS
    pattern = r"^(?:(?:[0-1]\d|2[0-3]):[0-5]\d:[0-5]\d|(?:(?:[0-5]?\d):)?[0-5]\d)$"
    # Check if the time string matches the pattern
    match = re.match(pattern, time)
    # Return True if match is found, False otherwise
    return match is not None


def extract_full_audio_validation(path: str, start_time: str) -> bool:
    if not os.path.exists(path):
        raise AudioExtractException(f"{path} was not found.")

    valid_media = ('video/mp4', 'audio/mpeg')
    type_check = magic.from_file(path, mime=True)
    if type_check not in valid_media:
        raise AudioExtractException(f"Invalid input file, {type_check} doesn't match video/audio media.")

    if not is_valid_hms(start_time):
        raise AudioExtractException(f"Invalid start time format, valid formats are \"HH:MM:SS\" or \"MM:SS\".")

    media_duration = utils.media_duration(path)
    formatted_media_duration = utils.seconds_to_hms(media_duration)

    start_time_seconds = utils.hms_to_seconds(start_time)
    if start_time_seconds > media_duration:
        raise AudioExtractException(
            f"Start time can't be bigger than input file duration \"{formatted_media_duration}\".")

    return True


def extract_sub_audio_validation(path: str, start_time: str, duration: str) -> bool:
    if not os.path.exists(path):
        raise AudioExtractException(f"{path} was not found.")

    type_check = magic.from_file(path, mime=True)
    if 'audio' not in type_check and 'video' not in type_check:
        raise AudioExtractException(f"Invalid input file, {type_check} doesn't match video/audio media.")

    if not is_valid_hms(start_time):
        raise AudioExtractException(f"Invalid start time format, valid formats are \"HH:MM:SS\" or \"MM:SS\".")

    if not is_valid_hms(duration):
        raise AudioExtractException(f"Invalid duration format, valid formats are \"HH:MM:SS\" or \"MM:SS\".")

    file_duration_seconds = utils.media_duration(path)
    formatted_media_duration = utils.seconds_to_hms(file_duration_seconds)

    start_time_seconds = utils.hms_to_seconds(start_time)
    if start_time_seconds > file_duration_seconds:
        raise AudioExtractException(
            f"Start time can't be bigger than input file duration \"{formatted_media_duration}\".")

    duration_seconds = utils.hms_to_seconds(duration)
    if duration_seconds > (file_duration_seconds - start_time_seconds):
        raise AudioExtractException(
            f"Invalid duration, new duration can't exceed file duration.")

    return True
