import speech_recognition as sr
import pyaudio
import os
import time
import wave
from playsound import playsound

def audiototext(audio):
    r = sr.Recognizer()
    with sr.AudioFile(audio) as source:
        audio = r.record(source)
        print ('Done!') 
    text = r.recognize_google(audio)
    
    return text
    


    
def recordaudio1():
    
    CHUNK = 1024 
    FORMAT = pyaudio.paInt16 #paInt8
    CHANNELS = 2 
    RATE = 44100 #sample rate
    RECORD_SECONDS = 10
    wave_file = "text"+".wav"
    WAVE_OUTPUT_FILENAME = wave_file

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK) #buffer

    print("* recording")
 
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data) # 2 bytes(16 bits) per channel

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    
    return wave_file

print(recordaudio1())