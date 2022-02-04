#!/bin/python3
# combine and modified codes from:
# https://github.com/quangthanh010290/voice_control_using_raspberry/blob/master/rpi_voice_control.py

import ctypes
import inspect
import os
import pyaudio
import speech_recognition as sr
#import threading
import time

for i, mic_name in enumerate (sr.Microphone.list_microphone_names()):
    print("mic: " + mic_name)
    # pulse seems better than usb mic
    if "ReSpeaker 4 Mic Array" in mic_name:
    #if "USB PnP Sound Device" in mic_name:
        mic = sr.Microphone(device_index=i, chunk_size=1024, sample_rate=48000)

pi_ear = sr.Recognizer()
pi_ear.dynamic_energy_threshold = True
pi_ear.non_speaking_duration= 0.1
pi_ear.pause_threshold = 0.1
#pi_ear.energy_threshold = 3000
while True:
	with mic as source:
	    pi_ear.adjust_for_ambient_noise(source, duration=0.5)
	    print("\033[0;35mpi: \033[0m I'm listening")
	    audio = pi_ear.listen(source, phrase_time_limit=2)
	print("finish listen")
	try:
	    you = pi_ear.recognize_google(audio)
	    #you = pi_ear.recognize_sphinx(audio,keyword_entries=[("help", 1.0)])
	except:
	    you = ""
	print(you)
	if "hello" in you:
	    print("hello detected, light led for several seconds")
        # need some led codes
	    time.sleep(2)
