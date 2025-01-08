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

st.markdown("**So funktioniert es:** Gib unterhalb einen LV-Titel (main title) und einen Titel für die Einheit (sub title) ein. Lade anschließend ein WAV-Podcast-File hoch. Dieses WAV-File erhältst du z.B. direkt von [Notebook LM](https://notebooklm.google.com/). Sobald du ein File ausgewählt hast, beginnt der Transformationsprozess. Aus dem WAV-File wird nun ein MP4-File erstellt. Wenn dieser Prozess abgeschlossen ist (kann ein paar Minuten dauern) erscheint unterhalb ein **Download-Button**. Nun kannst du dein MP4-File herunterladen.")
st.markdown("So sieht dein fertiges Video aus:")

st.image("static/demo.png", "Demo image of output file")

main_title = st.text_input("Main Title (see demo image)")
sub_title = st.text_input("Sub Title (see demo image)")
file = st.file_uploader("WAV File", type=["wav"])

new_title = main_title.replace(" ", "_")+"___"+sub_title.replace(" ", "_")+".mp4"

if file is not None:
    if isfile("temp.wav"):
        remove("temp.wav")

    with open("temp.wav", 'bx') as f:
        f.write(file.read())

    if isfile("temp.mp4"):
        remove("temp.mp4")

    mp3_to_mp4("temp.wav", main_title, sub_title)
    remove("temp.wav")

    with open("temp.mp4", 'rb') as f:
        st.download_button('Download MP4-File', f, file_name=new_title)