import os
import argparse
import mimetypes
from moviepy.editor import VideoFileClip


def check_filepath(path: str):
    # Check if valid file
    if not os.path.isfile(path):
        raise FileNotFoundError('Make sure the file path is correct')
    # Check if file is of type video
    if not mimetypes.guess_type(path)[0].startswith('video'):
        raise TypeError('This file is not of type video')


def check_savepath(path: str):
    if path == './':
        return
    print(path)
    if not os.path.isdir(path):
        raise Exception("Make sure your save path is correct (It shouldn't contain a filename)")
    if not os.path.isdir(path):
        os.makedirs(path)


def get_filename(filename: str, filepath: str) -> str:
    if filename:
        if filename.endswith('.mp3'):
            return filename
        else:
            return filename + ".mp3"

    original_file = filepath.split("\\")[-1]
    original_name = original_file.split(".")[0]
    return original_name + ".mp3"


def is_full_audio(start, end):
    if start is None or end is None:
        return True

    if type(start) is not float or type(end) is not float:
        raise TypeError("Make sure start and end time are float numbers")

    return False


def extract_audio(filepath, savepath="./new.mp3", full_audio=True, timestamps: tuple[float, float] = (0.0, 0.0)):
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
            video_file = VideoFileClip(filepath)
            sub_clip = video_file.subclip(*timestamps)
            file_audio = sub_clip.audio
            file_audio.write_audiofile(savepath)
            print(f'Audio successfully saved to {savepath}')
        except Exception as e:
            print(f"Something went wrong while extracting file audio, {e}")


def main():
    # --- Arguments Parser ---
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', help='Path to the video file', required=True, type=str)
    parser.add_argument('--save-path', help='Save path for the created mp3 file (Do not include filename here)',
                        default="./", type=str)
    parser.add_argument('--filename', help='Save name of the created mp3 file', type=str)
    parser.add_argument('--start', help='Starting second of the desired audio', type=float)
    parser.add_argument('--end', help='Ending second of the desired audio', type=float)
    args = parser.parse_args()
    # --- Application Vars ---
    FILE_PATH = os.path.abspath(args.path)
    SAVE_PATH = os.path.abspath(args.save_path)
    FILENAME = args.filename
    START = args.start
    END = args.end
    # --- Validate Vars ---
    check_filepath(FILE_PATH)
    check_savepath(SAVE_PATH)
    filename = get_filename(FILENAME, FILE_PATH)
    save_path = os.path.join(SAVE_PATH, filename)
    full_audio = is_full_audio(START, END)
    timestamps = (START, END)
    # --- Extract audio ---
    if full_audio:
        extract_audio(filepath=FILE_PATH,
                      savepath=save_path,
                      full_audio=full_audio)
    else:
        extract_audio(filepath=FILE_PATH,
                      savepath=save_path,
                      full_audio=full_audio,
                      timestamps=timestamps)


if __name__ == '__main__':
    main()
