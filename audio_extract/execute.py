#!/usr/bin/env python

import argparse
from audio_extract import extract_audio


def main():
    # Create the parser
    parser = argparse.ArgumentParser()
    # Add the arguments
    parser.add_argument('--input', '-i',
                        help='The path to the video/audio input file.',
                        required=True, type=str)
    parser.add_argument('--output', '-o',
                        help='The path to the extracted audio file.',
                        default='./audio.mp3', type=str)
    parser.add_argument('--format', '-f',
                        help='The format of the extracted audio file. '
                             'Only (wav, ogg, mp3, aac, flac, m4a, oga, opus) are supported',
                        default='mp3', type=str)
    parser.add_argument('--start-time', '-st',
                        help='The start time of the extracted audio \"HH:MM:SS\" or \"MM:SS\" format.',
                        default='00:00:00', type=str)
    parser.add_argument('--duration', '-d',
                        help='The duration of the extracted audio in seconds.', type=float, default=None)
    parser.add_argument('--overwrite', '-ow', help='Overwrite the output file if it exists.', type=bool, default=False)
    # Parse the arguments
    args = parser.parse_args()
    input_path = args.input
    output_path = args.output
    output_format = args.format
    start_time = args.start_time
    duration = args.duration
    overwrite = args.overwrite

    extract_audio(input_path=input_path, output_path=output_path, output_format=output_format, start_time=start_time,
                  duration=duration,
                  overwrite=overwrite)


if __name__ == '__main__':
    main()
