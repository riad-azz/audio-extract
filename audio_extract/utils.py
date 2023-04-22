import mutagen


def print_success(text: str):
    print("\033[32m" + "✅  " + f"{text}" + "\033[0m")


def print_error(text: str):
    print("\033[31m" + "❌  " + f"{text}" + "\033[0m")


def media_duration(path: str):
    file = mutagen.File(path)
    duration = file.info.length
    return duration


def seconds_to_hms(seconds: float | int) -> str:
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    hms = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
    return hms


def hms_to_seconds(time_str) -> float | None:
    # Split the time string into hours, minutes, and seconds
    time_parts = time_str.split(':')
    if len(time_parts) == 3:  # HH:MM:SS format
        hours, minutes, seconds = map(int, time_parts)
    elif len(time_parts) == 2:  # MM:SS format
        hours = 0
        minutes, seconds = map(int, time_parts)
    else:
        print_error("Invalid time format. Must be in HH:MM:SS or MM:SS format.")
        return None

    # Calculate the total number of seconds
    total_seconds = hours * 3600 + minutes * 60 + seconds

    # Return the total number of seconds as a float
    return float(total_seconds)
