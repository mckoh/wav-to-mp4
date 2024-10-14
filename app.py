import streamlit as st
from mp3_to_mp4 import mp3_to_mp4
from tempfile import NamedTemporaryFile
from os import remove
from os.path import isfile

st.set_page_config(
    page_icon="🤖",
    page_title="MP4 Generator",
)

st.title("MP4 Generator")

st.image("static/demo.png", "Demo image of output file")

main_title = st.text_input("Main Title (see demo image)")
sub_title = st.text_input("Sub Title (see demo image)")
file = st.file_uploader("WAV File", type=["wav"])

if file is not None:
    with open("temp.wav", 'bx') as f:
        f.write(file.read())

    if isfile("temp.mp4"):
        remove("temp.mp4")

    mp3_to_mp4("temp.wav", main_title, sub_title)
    remove("temp.wav")
    with open('temp.mp4', 'rb') as f:
        st.download_button('Download Video', f, file_name='temp.mp4')