import re
import os
from audio_extract import utils

SUPPORTED_AUDIO_FORMATS = [
    'wav', 'ogg', 'mp3', 'aac', 'flac', 'm4a', 'oga', 'opus'
]

SUPPORTED_VIDEO_FORMATS = [
    'mp4', 'mkv', 'webm', 'flv', 'avi', 'mov', 'wmv', 'm4v'
]

SUPPORTED_FFMPEG_FORMATS = SUPPORTED_AUDIO_FORMATS + SUPPORTED_VIDEO_FORMATS


class AudioExtractValidator:

    def __init__(self, input_path: str, output_path: str, output_format: str, duration: float, start_time: str,
                 overwrite: bool):
        self.input_path = input_path
        self.output_path = output_path
        self.output_format = output_format
        self.duration = duration
        self.start_time = start_time
        self.overwrite = overwrite

    def validate(self) -> dict:
        # Validate and clean all inputs
        self._validate_input_path()
        self._validate_output_format()
        self._validate_output_path()
        self._validate_start_time()
        self._validate_duration()
        # Return cleaned and validated inputs
        return self.__dict__

    def _validate_input_path(self):
        input_path = os.path.abspath(self.input_path)

        if not any(input_path.endswith("." + x) for x in SUPPORTED_FFMPEG_FORMATS):
            raise Exception(f"Input file format not supported. Only (Video/Audio) allowed.")

        if not os.path.isfile(input_path):
            raise Exception(f"{input_path} was not found, please provide a valid file path.")

        self.input_path = input_path

    def _validate_output_path(self):
        output_path = self.output_path
        if output_path.endswith("/") or output_path.endswith("\\"):
            output_path += "audio." + self.output_format

        output_path = os.path.abspath(output_path)
        output_parts = output_path.split(os.sep)
        filename = output_parts[-1]
        folder_path = f"{os.sep}".join(output_parts[:-1])

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        extension = "." + self.output_format
        if not filename.endswith(extension):
            output_path = output_path + extension

        if os.path.isfile(output_path) and not self.overwrite:
            raise Exception(f"File already exists in output path: {output_path}.")

        self.output_path = output_path

    def _validate_output_format(self):
        output_format = self.output_format
        if output_format not in SUPPORTED_AUDIO_FORMATS:
            supported_formats = ', '.join(SUPPORTED_AUDIO_FORMATS)
            raise Exception(f"Output format {self.output_format} not supported, Only ({supported_formats}) are supported")

    def _validate_start_time(self):
        start_time = self.start_time

        pattern = r"^(?:(\d{1,2}):)?(\d{1,2}):(\d{1,2})$"
        if not re.match(pattern, start_time):
            raise Exception("Invalid time format. Must be in HH:MM:SS or MM:SS format.")

        file_duration = utils.media_duration(self.input_path)
        start_time_seconds = utils.hms_to_seconds(self.start_time)
        if start_time_seconds > file_duration:
            raise Exception("Start time can't be longer than the input (Video/Audio) file duration")

        self.start_time = start_time

    def _validate_duration(self):
        if not self.duration:
            return

        duration = self.duration
        if duration == 0:
            raise Exception("Duration can't be 0")
        elif duration < 0:
            raise Exception("Duration can't be negative")

        file_duration = utils.media_duration(self.input_path)
        start_time_seconds = utils.hms_to_seconds(self.start_time)
        time_sum = duration + start_time_seconds
        if time_sum > file_duration:
            raise Exception("Duration can't be longer than the input (Video/Audio) file duration")

        self.duration = str(duration)
