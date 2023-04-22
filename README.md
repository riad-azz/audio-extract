# Python Audio Extract

Extract audio from videos or trim audio/video audio

## Description

Python Audio Extract allows you to extract audio from video files and trim the audio according to your needs.
It supports various video and audio formats and has a simple and user-friendly interface.

It can also be used to trim audios.

## Installing

```bash
git clone https://github.com/riad-azz/py-audio-extract.git
```

```bash
cd py-audio-extract
```

```bash
pip install -r requirements.txt
```

```bash
pip install python-magic-bin --force
```

*Note : because of library conflicts between python-magic and python-magic-bin they have to be installed separately*

## Executing the program

### CLI Arguments

The following cli arguments are supported:

* **`--input`** or **`-i`**

The path to the video/audio input file.

* **`--output`** or **`-o`**

The path to the mp3 output file. The default value is `./audio.mp3`.

* **`--start`** or **`-s`**

The start time of the output in `HH:MM:SS` or `MM:SS` format. The default value is `00:00`.

* **`--duration`**

The duration of the output in `HH:MM:SS` or `MM:SS` format.

### Extract full audio

```bash
python run.py --input video.mp4 --output audio.mp3
```

This would create a mp3 file called `audio.mp3` that contains the full audio of the video file `video.mp4`.

#### Extract sub clip audio

```bash
python run.py --input video.mp4 --output audio.mp3 --start 00:00:30
```

This would create a mp3 file called `audio.mp3` that starts after the first 30 seconds of the video file `video.mp4`.

#### Extract sub clip audio with custom duration

```bash
python run.py --input video.mp4 --output audio.mp3 --start '00:25' --duration '01:15'
```

This command will convert video file `video.mp4` to a mp3 file starting from `00:25` to `01:15`
called `audio.mp3` that will have a duration of `00:50`.

#### Trim audio

```bash
python run.py --input audio.mp3 --output new_audio.mp3 --start '00:05' --duration '01:15'
```

This command trim the audio starting from `00:05` to `01:15` of the file `audio.mp3` to a mp3 file
called `new_audio.mp3` that will have a duration of `01:10`.

### Script example

```python
import audio_extract

if __name__ == "__main__":
    audio_extract.run(
        input_path="./video.mp4",
        output_path="./audio.mp3",
        start_time="00:15",
        duration="05:35",
    )
```

## License

This project is licensed under the [MIT] License - see the LICENSE.md file for details