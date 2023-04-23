# Audio Extract

audio-extract is a Python library that allows you to extract audio from video files and trim the audio according to your
needs

## Description

audio-extract is a Python library that allows you to extract audio from video files and trim the audio according to your
needs. You can use it to create audio clips from movies, podcasts, or any other video source. It supports various audio
and video formats, such as MP3, WAV, OGG, MP4, AVI, and MKV.

## Installing

```bash
pip install audio-extract
```

## Executing the program

#### Extract full audio

```python
import audio_extract as audio_extract

audio_extract.run(input_path="./video.mp4", output_path="./audio.mp3")
```

This will create a mp3 file called `audio.mp3` that contains the full audio of the video file `video.mp4`.

#### Extract sub clip audio

```python
import audio_extract as audio_extract

audio_extract.run(input_path="./video.mp4", output_path="./audio.mp3", start_time="00:30")
```

This will create a mp3 file called `audio.mp3` that starts after the first 30 seconds of the video file `video.mp4`.

#### Extract sub clip audio with custom duration

```python
import audio_extract

audio_extract.run(input_path="./video.mp4", output_path="./audio.mp3", start_time="00:25", duration="01:15")
```

This will convert video file `video.mp4` to a mp3 file starting from `00:25` to `01:15`
called `audio.mp3` that will have a duration of `00:50`.

#### Trim audio

```python
import audio_extract

audio_extract.run(input_path="./audio.mp3", output_path="./new_audio.mp3", start_time="00:05", duration="01:15")
```

This will trim the `audio.mp3` file starting from `00:05` to `01:15`  to a mp3 file called `new_audio.mp3` that will
have a duration of `01:10`.

## Running Command-Line-Interface

### CLI Arguments

The following cli arguments are supported:

* **`--input`** or **`-i`**

The path to the video/audio input file.

* **`--output`** or **`-o`**

The path to the mp3 output file. The default value is `./audio.mp3`.

* **`--start`** or **`-s`**

The start time of the output in `HH:MM:SS` or `MM:SS` format. The default value is `00:00`.

* **`--duration`** or **`-d`**

The duration of the output in `HH:MM:SS` or `MM:SS` format.

### Extract full audio

```bash
audio-extract --input video.mp4 --output audio.mp3
```

This command will create a mp3 file called `audio.mp3` that contains the full audio of the video file `video.mp4`.

#### Extract sub clip audio

```bash
audio-extract --input video.mp4 --output audio.mp3 --start 00:00:30
```

This would create a mp3 file called `audio.mp3` that starts after the first 30 seconds of the video file `video.mp4`.

#### Extract sub clip audio with custom duration

```bash
audio-extract --input video.mp4 --output audio.mp3 --start '00:25' --duration '01:15'
```

This command will convert video file `video.mp4` to a mp3 file starting from `00:25` to `01:15`
called `audio.mp3` that will have a duration of `00:50`.

#### Trim audio

```bash
audio-extract --input audio.mp3 --output new_audio.mp3 --start '00:05' --duration '01:15'
```

This command trim the audio starting from `00:05` to `01:15` of the file `audio.mp3` to a mp3 file
called `new_audio.mp3` that will have a duration of `01:10`.

## Authors

Riadh Azzoun - [@riad-azz](https://github.com/riad-azz)

## License

This project is licensed under the [MIT] License - see the LICENSE.md file for details