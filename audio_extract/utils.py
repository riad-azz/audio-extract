import mutagen


def media_duration(file_path: str):
    file = mutagen.File(file_path)
    duration = file.info.length
    return duration


def seconds_to_hms(seconds: float | int) -> str:
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    hms = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
    return hms


def hms_to_seconds(time_str: str) -> float:
    # Split the time string into hours, minutes, and seconds
    time_parts = time_str.split(':')
    if len(time_parts) == 3:  # HH:MM:SS format
        hours, minutes, seconds = map(int, time_parts)
    elif len(time_parts) == 2:  # MM:SS format
        hours = 0
        minutes, seconds = map(int, time_parts)
    else:
        raise Exception("Invalid time format. Must be in HH:MM:SS or MM:SS format.")

    # Calculate the total number of seconds
    total_seconds = hours * 3600 + minutes * 60 + seconds

    # Return the total number of seconds as a float
    return float(total_seconds)
