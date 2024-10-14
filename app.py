import streamlit as st
from mp3_to_mp4 import mp3_to_mp4
from tempfile import NamedTemporaryFile
from os import remove

remove("test.mp4")

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
    with open("test.wav", 'bx') as f:
        f.write(file.read())
    mp3_to_mp4("test.wav", main_title, sub_title)
    remove("test.wav")
    with open('test.mp4', 'rb') as f:
        st.download_button('Download Video', f, file_name='test.mp4')