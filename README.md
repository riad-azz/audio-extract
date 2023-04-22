# Python Audio Extract

Extract audio from videos or trim audio/videos audio

## Getting Started

### Installing

```
git clone https://github.com/riad-azz/py-audio-extract.git
```

```
cd py-audio-extract
```

```
pip install -r requirements.txt
```

### Executing the program 

#### Extracting full audio

```python
python run.py --input='./video.mp4' --output='./audio.mp3'
```

#### Extracting audio from sub clip

```python
python run.py --input='./video.mp4' --output='./audio.mp3' --start='00:05' --duration='01:15'
```

E.g. if the input file duration is "02:20" then output file will be starting from "00:05" up to "1:20".

#### Script example

```python
import audio_extract

if __name__ == '__main__':
    audio_extract.run(input_path='./video.mp4',
                      output_path='./audio.mp3',
                      start_time='00:15',
                      duration='05:35')
```
