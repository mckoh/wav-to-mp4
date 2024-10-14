# %%
from moviepy.editor import AudioFileClip, ImageClip
from sys import argv
from os import remove
from pydub import AudioSegment

# %%
def wav_to_mp3(wav_file_path):
    mp3_file_path = wav_file_path.split(".")[0]+".mp3"

    print(wav_file_path, mp3_file_path)

    sound = AudioSegment.from_wav(wav_file_path)
    sound.export(mp3_file_path, format="mp3")
    return mp3_file_path

#%%
def mp3_to_mp4(wav_file_path, png_file_path):

    mp3_file_path = wav_to_mp3(wav_file_path)
    audio_clip = AudioFileClip(mp3_file_path)
    image_clip = ImageClip(png_file_path)

    file_name = mp3_file_path.split(".")[0]

    video_clip = image_clip.set_audio(audio_clip)
    video_clip.duration = audio_clip.duration
    video_clip.fps = 30
    video_clip.write_videofile(file_name+'.mp4')

    remove(mp3_file_path)

    return True

if __name__ == "__main__":
    print(
        mp3_to_mp4("relationship_advanced.wav", "image.png")
    )