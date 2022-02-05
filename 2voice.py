#!/bin/python3

# modified codes from:
# https://github.com/quangthanh010290/voice_control_using_raspberry/blob/master/rpi_voice_control.py

import ctypes
import inspect
import os
import pyaudio
import speech_recognition as sr
#import threading
import time

def callback(self, audio):
    print("start recognize")
    try:
        you = rec.recognize_google(audio)
        #you = rec.recognize_sphinx(audio, keyword_entries=[("help", 1.0),("start", 1.0)])
    except:
        you = ""
    print("finish recognize, your speech is: ", you)
    if "hello" in you:
        print("hello detected, start led for several seconds")
        #start_led()
        #time.sleep(2)

for i, mic_name in enumerate (sr.Microphone.list_microphone_names()):
    print("mic: " + mic_name)
    # pulse seems better than usb mic
    if "pulse" in mic_name:
    #if "USB PnP Sound Device" in mic_name:
        mic = sr.Microphone(device_index=i, chunk_size=1024, sample_rate=48000)

rec = sr.Recognizer()
rec.dynamic_energy_threshold = True
rec.non_speaking_duration= 0.1
rec.pause_threshold = 0.1
#rec.energy_threshold = 3000
with mic as source:
    rec.adjust_for_ambient_noise(source, duration=0.5)
rec.listen_in_background(mic, callback, phrase_time_limit=2)
while True:
    time.sleep(0.1)
