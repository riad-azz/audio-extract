# Other modules
import subprocess
import imageio_ffmpeg

# Local modules
from audio_extract.validators import AudioExtractValidator

FFMPEG_BINARY = imageio_ffmpeg.get_ffmpeg_exe()


def extract_audio(input_path: str, output_path: str = "./audio.mp3", output_format: str = "mp3",
                  start_time: str = "00:00:00",
                  duration: float = None,
                  overwrite: bool = False):
    validator = AudioExtractValidator(input_path, output_path, output_format, duration, start_time, overwrite)
    result = validator.validate()

    cleaned_input_path = result["input_path"]
    cleaned_output_path = result["output_path"]
    cleaned_output_format = result["output_format"]
    cleaned_start_time = result["start_time"]
    cleaned_duration = result["duration"]

    command = [FFMPEG_BINARY,
               '-i', cleaned_input_path,
               '-ss', cleaned_start_time,
               '-f', cleaned_output_format,
               '-y', cleaned_output_path]

    if cleaned_duration:
        command.insert(3, "-t")
        command.insert(4, cleaned_duration)

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        print(f"Success : audio file has been saved to \"{cleaned_output_path}\".")
    else:
        error = result.stderr.decode().strip().split("\n")[-1]
        raise Exception(f"Failed : {error}.")
