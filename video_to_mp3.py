from moviepy.editor import VideoFileClip


def extract_audio(filepath, savepath="./new.mp3", full_audio=True,
                  timestamps: tuple[float | None, float | None] = (0.0, 0.0)):
    if full_audio:
        try:
            video_file = VideoFileClip(filepath)
            file_audio = video_file.audio
            file_audio.write_audiofile(savepath)
            print(f'Audio successfully saved to {savepath}')
        except Exception as e:
            print(f"Something went wrong while extracting file audio, {e}")
    else:
        try:
            start, end = timestamps
            video_file = VideoFileClip(filepath)
            end = video_file.duration if not end else end
            start = 0 if not start else start
            sub_clip = video_file.subclip(start, end)
            file_audio = sub_clip.audio
            file_audio.write_audiofile(savepath)
            print(f'Audio successfully saved to {savepath}')
        except Exception as e:
            print(f"Something went wrong while extracting file audio, {e}")
