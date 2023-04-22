#!/usr/bin/env python

import argparse
import audio_extract


def main():
    # Create the parser
    parser = argparse.ArgumentParser()
    # Add the arguments
    parser.add_argument('--input', "-i",
                        help='The path to the video/audio input file.',
                        required=True, type=str)
    parser.add_argument('--output', "-o",
                        help='The path to the mp3 output file.',
                        default="./audio.mp3", type=str)
    parser.add_argument('--start', "-s", help='The start time of the output "HH:MM:SS" or "MM:SS" format.',
                        default="00:00", type=str)
    parser.add_argument('--duration', "-d",
                        help='The duration of the output "HH:MM:SS" or "MM:SS" format.', type=str)
    # Parse the arguments
    args = parser.parse_args()
    input_path = args.input
    output_path = args.output
    start_time = args.start
    duration = args.duration

    audio_extract.run(input_path, output_path, start_time=start_time, duration=duration)


if __name__ == '__main__':
    main()
