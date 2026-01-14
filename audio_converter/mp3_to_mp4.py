from moviepy.editor import AudioFileClip, ImageClip
from sys import argv
from os import remove
from pydub import AudioSegment
from PIL import Image, ImageDraw, ImageFont


def place_title(main_title, sub_title, image_path):
    input_image = Image.open('static/background.png')
    working_image = ImageDraw.Draw(input_image)
    h1_font = ImageFont.truetype('static/franklin_demi.ttf', 66)
    h2_font = ImageFont.truetype('static/franklin_regular.ttf', 28)
    working_image.text((660, 480), main_title, font=h1_font, fill=(255, 255, 255))
    working_image.text((660, 560), sub_title, font=h2_font, fill=(255, 255, 255))
    input_image.save(image_path)
    return image_path


def wav_to_mp3(wav_file_path):
    mp3_file_path = wav_file_path.split(".")[0]+".mp3"
    sound = AudioSegment.from_wav(wav_file_path)
    sound.export(mp3_file_path, format="mp3")
    return mp3_file_path


def m4a_to_mp3(m4a_file_path):
    mp3_file_path = m4a_file_path.split(".")[0]+".mp3"
    sound = AudioSegment.from_file(m4a_file_path)
    sound.export(mp3_file_path, format="mp3")
    return mp3_file_path


def convert(file_path, main_title, sub_title):
    file_name = file_path.split(".")[0]
    file_extension = file_path.split(".")[1]

    if file_extension == "wav":
        file_path = wav_to_mp3(file_path)

    if file_extension == "m4a":
        file_path = m4a_to_mp3(file_path)

    audio_clip = AudioFileClip(file_path)

    png_file_path = place_title(
        main_title=main_title,
        sub_title=sub_title,
        image_path=file_name+".png"
    )

    image_clip = ImageClip(png_file_path)
    video_clip = image_clip.set_audio(audio_clip)
    video_clip.duration = audio_clip.duration
    video_clip.fps = 30
    video_clip.write_videofile(file_name+'.mp4')

    try:
        remove(file_path)
        remove(png_file_path)
    except:
        pass

    return True
