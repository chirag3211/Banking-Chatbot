import json
import wave
import speech_recognition as sr

sample_rate=44100
text=None
running = None

r=sr.Recognizer()
def recognize():
    with sr.Microphone(device_index=1) as source:
        print("Listening...")
        # r.pause_threshold=1
        r.pause_threshold=0.5
        audio=r.listen(source)

    query=r.recognize_google(audio,language='en-in')
    print(query)
    return query

