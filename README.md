# Audio Extract

audio-extract is a Python library that allows you to extract audio from video files and trim the audio according to your
needs

## Description

audio-extract is a Python library that allows you to extract audio from video files and trim the audio according to your
needs. You can use it to create audio clips from movies, podcasts, or any other video source. It supports various audio
and video formats, such as MP3, WAV, OGG, MP4, AVI, and MKV.

## Installing

- Install from Pypi:

```bash
pip install audio-extract
```

- Install from GitHub:

```bash
pip install git+https://github.com/riad-azz/audio-extract.git
```

## Getting Started

### AudioExtract - Info

The application is pretty straightforward all you need is to import the `extract_audio` function. The function args:

* **`input_path`** : The path to the input (Video/Audio) file.

* **`output_path`**: The path to the extracted audio file. The default value is `./audio.mp3`.

* **`output_format`**: The format of the extracted audio. The default value is `mp3`.

* **`start_time`**: The start time of the output in `HH:MM:SS` or `MM:SS` format. The default value is `00:00:00`.

* **`duration`**: The duration of the extracted audio in seconds _(float)_. The default value is  `None` which means
  full audio will be extracted if `start_time` is set to `00:00:00`.

* **`overwrite`**: Whether to overwrite the output file if it already exists or not. The default value is `False`.

The supported file formats:

- Supported audio formats : `WAV, OGG, MP3, AAC, FLAC, M4A, OGA, OPUS`

- Supported video formats : `MP4, MKV, WEBM, FLV, AVI, MOV, WMV, M4V`

### Executing the program

- Extract full audio:

```python
from audio_extract import extract_audio

extract_audio(input_path="./video.mp4", output_path="./audio.mp3")
```

This will create a `mp3` file called `audio.mp3` that contains the full audio of the video file `video.mp4`.

- Extract sub clip audio:

```python
from audio_extract import extract_audio

extract_audio(input_path="./video.mp4", output_path="./audio.mp3", start_time="00:30")
```

This will create a `mp3` file called `audio.mp3` that starts after the first 30 seconds of the video file `video.mp4`.

- Extract sub clip audio with custom duration

```python
from audio_extract import extract_audio

extract_audio(input_path="./video.mp4", output_path="./audio.mp3", start_time="00:25", duration=15.0)
```

This will convert video file `video.mp4` to a mp3 file starting from `00:25` to `00:40`
called `audio.mp3` that will have a duration of `00:15`.

- Trim audio:

```python
from audio_extract import extract_audio

extract_audio(input_path="./audio.mp3", output_path="./new_audio.mp3", start_time="00:05", duration=20.0)
```

This will trim the `audio.mp3` file starting from `00:05` to `00:25` to a `mp3` file called `new_audio.mp3` that will
have a duration of `00:20`.

## Running Command-Line-Interface

### CLI Arguments

The following cli arguments are supported:

* **`--input`** or **`-i`** : The path to the input (Video/Audio) file.

* **`--output`** or **`-o`** : The path to the extracted audio file. The default value is `./audio.mp3`.

* **`--format`** or **`-f`** : The format of the extracted audio. The default value is `mp3`.

* **`--start-time`** or **`-st`** : The start time of the output in `HH:MM:SS` or `MM:SS` format. The default value
  is `00:00:00`.

* **`--duration`** or **`-d`** : The duration of the extracted audio in seconds _(float)_, The default value is `None`
  which means full audio will be extracted if `start_time` is set to `00:00:00`.

* **`--overwrite`** or **`-ow`** : Whether to overwrite the output file if it already exists or not. The default value
  is `False`.

### CLI Usage Example:

Here is an example of using the CLI to extract audio:

```bash
audio-extract --input="./video.mp4" --output="./audios/extracted_audio.wav" --format="wav"
```

This command will extract the full audio starting from `video.mp4` to a `wav` file called `extracted_audio.wav` and will
be saved to the folder `./audios/`. The folder will be automatically created if it doesn't exist.

## Authors

Riadh Azzoun - [@riad-azz](https://github.com/riad-azz)

## License

This project is licensed under the [MIT] License - see the LICENSE.md file for details