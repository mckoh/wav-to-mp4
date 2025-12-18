from os import remove
from os.path import isfile


def clean():
    if isfile("temp.wav"):
        remove("temp.wav")

    if isfile("temp.mp3"):
        remove("temp.mp3")

    if isfile("temp.mp4"):
        remove("temp.mp4")

    if isfile("temp.m4a"):
        remove("temp.m4a")