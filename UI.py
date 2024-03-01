import streamlit as st
# from sa.audio_recorder_streamlit import audio_recorder
# from SAR.st_audiorec import st_audiorec
import os
# import uuid
from speech2text import *
import subprocess
from run_test5 import banking_bot

# def get_recently_modified_file(directory):
#     files = os.listdir(directory)

#     files = [os.path.join(directory, f) for f in files if os.path.isfile(os.path.join(directory, f))]
#     file_modification_times = [(f, os.path.getmtime(f)) for f in files]

#     file_modification_times.sort(key=lambda x: x[1], reverse=True)

#     if file_modification_times:
#         return file_modification_times[0][0]
#     else:
#         return None


st.title("Banking Talking Assistant")
st.title("Audio Recorder")
# audio0 = audiorecorder("Click to record", "Click to stop recording")

"""
Hi🤖 just click on the voice recorder and let me know how I can help you today?
"""

# wav_audio_data = st_audiorec()

# if wav_audio_data is not None:
#     st.audio(wav_audio_data, format='audio/wav')

if st.button('start recording'):
    txt1 = recognize()

ee =banking_bot(txt1)



def execute_python_file(file_path):
    try:
        subprocess.run(["python3", file_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing {file_path}: {e}")



# audio_location = os.path.dirname(os.path.abspath(__file__))
# directory_path = f'{audio_location}\piper\audio'
# recent_file = get_recently_modified_file(directory_path)

if st.button('play audio'):
    with open('C:/ass/Banking_Chatbot/piper/text/Demo.txt', 'w') as f:
        f.write(ee)
    execute_python_file('C:/ass/Banking_Chatbot/piper/piper.py')
    audio_file = open('C:/ass/Banking_Chatbot/piper/audio/dd.wav', 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='wav')
