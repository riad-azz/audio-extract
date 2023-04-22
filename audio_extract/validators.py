import os
import re
import magic
from audio_extract import utils


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
        utils.print_error(f"{path} was not found.")
        return False

    valid_media = ('video/mp4', 'audio/mpeg')
    if not magic.from_file(path, mime=True) in valid_media:
        utils.print_error(f"Invalid input file, doesn't match video/audio media.")
        return False

    if not is_valid_hms(start_time):
        utils.print_error(f"Invalid start time format, valid formats are \"HH:MM:SS\" or \"MM:SS\".")
        return False

    media_duration = utils.media_duration(path)
    formatted_media_duration = utils.seconds_to_hms(media_duration)

    start_time_seconds = utils.hms_to_seconds(start_time)
    if start_time_seconds is None:
        return False
    if start_time_seconds > media_duration:
        utils.print_error(
            f"Start time can't be bigger than input file duration \"{formatted_media_duration}\".")
        return False

    return True


def extract_sub_audio_validation(path: str, start_time: str, duration: str) -> bool:
    if not os.path.exists(path):
        utils.print_error(f"{path} was not found.")
        return False

    valid_media = ('video/mp4', 'audio/mpeg')
    if not magic.from_file(path, mime=True) in valid_media:
        utils.print_error(f"Invalid input file, doesn't match video/audio media.")
        return False

    if not is_valid_hms(start_time):
        utils.print_error(f"Invalid start time format, valid formats are \"HH:MM:SS\" or \"MM:SS\".")
        return False

    if not is_valid_hms(duration):
        utils.print_error(f"Invalid duration format, valid formats are \"HH:MM:SS\" or \"MM:SS\".")
        return False

    file_duration_seconds = utils.media_duration(path)
    formatted_media_duration = utils.seconds_to_hms(file_duration_seconds)

    start_time_seconds = utils.hms_to_seconds(start_time)
    if start_time_seconds is None:
        return False
    if start_time_seconds > file_duration_seconds:
        utils.print_error(
            f"Start time can't be bigger than input file duration \"{formatted_media_duration}\".")
        return False

    duration_seconds = utils.hms_to_seconds(duration)
    if duration_seconds is None:
        return False
    if duration_seconds > (file_duration_seconds - start_time_seconds):
        utils.print_error(
            f"Invalid duration, new duration can't exceed file duration.")
        return False

    return True
