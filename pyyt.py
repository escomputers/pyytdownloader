"""Script to download youtube videos as .wav"""
from __future__ import unicode_literals

import sys

import ffmpeg
import yt_dlp

ydl_opts = {
    "format": "bestaudio/best",
    #    'outtmpl': 'output.%(ext)s',
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "wav",
        }
    ],
}


def download_from_url(yturl):
    """Function to convert .m4a to .wav"""
    ydl.download([yturl])
    stream = ffmpeg.input("output.m4a")
    stream = ffmpeg.output(stream, "output.wav")


with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    args = sys.argv[1:]
    if len(args) > 1:
        print("Too many arguments.")
        print("Usage: python pyyt.py <optional link>")
        sys.exit()
    if len(args) == 0:
        url = input("Enter Youtube URL: ")
        download_from_url(url)
    else:
        download_from_url(args[0])
