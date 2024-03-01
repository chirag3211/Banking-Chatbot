from speech2text import *
import subprocess
from run_test5 import banking_bot
import os
import winsound
import sounddevice as sd
 
# from pydub import AudioSegment
# from pydub.playback import play
 
def execute_python_file(file_path):
    try:
        subprocess.run(["python", file_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing {file_path}: {e}")

def play_audio_file(audio_file_path):
    try:
        winsound.PlaySound(audio_file_path, winsound.SND_FILENAME)
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    while True:
        txt1 = recognize()
        ee =banking_bot(txt1)
        print(ee)
        with open('C:/ass/Banking_Chatbot/piper/text/Demo.txt', 'w') as f:
            f.write(ee)
        execute_python_file('C:/ass/Banking_Chatbot/piper/piper.py')
        play_audio_file('C:/ass/Banking_Chatbot/piper/audio/dd.wav')
        # tape = AudioSegment.from_file('C:/ass/Banking_Chatbot/piper/audio/dd.wav', format='wav')
        # tape = AudioSegment.from_wav('C:/ass/Banking_Chatbot/piper/audio/dd.wav')
 
        # play(tape)