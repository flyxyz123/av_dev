#!/bin/python3

# modified codes from:
# https://github.com/quangthanh010290/voice_control_using_raspberry/blob/master/rpi_voice_control.py
# https://github.com/respeaker/pixel_ring/blob/master/pixel_ring/usb_pixel_ring_v2.py

import ctypes
import inspect
import os
import pyaudio
import speech_recognition as sr
#import threading
import time
#import usb.core
#import usb.util
import RPi.GPIO as GPIO

LAMP_PIN_ARR = [17, 27, 22, 10, 9, 11]

#class PixelRing:
#    TIMEOUT = 8000
#    def __init__(self, dev):
#        self.dev = dev
#    def trace(self):
#        self.write(0)
#    def mono(self, color):
#        self.write(1, [(color >> 16) & 0xFF, (color >> 8) & 0xFF, color & 0xFF, 0])
#    def set_color(self, rgb=None, r=0, g=0, b=0):
#        if rgb:
#            self.mono(rgb)
#        else:
#            self.write(1, [r, g, b, 0])
#    def off(self):
#        self.mono(0)
#    def listen(self, direction=None):
#        self.write(2)
#    wakeup = listen
#    def speak(self):
#        self.write(3)
#    def think(self):
#        self.write(4)
#    wait = think
#    def spin(self):
#        self.write(5)
#    def show(self, data):
#        self.write(6, data)
#    customize = show
#    def set_brightness(self, brightness):
#        self.write(0x20, [brightness])
#    def set_color_palette(self, a, b):
#        self.write(0x21, [(a >> 16) & 0xFF, (a >> 8) & 0xFF, a & 0xFF, 0, (b >> 16) & 0xFF, (b >> 8) & 0xFF, b & 0xFF, 0])
#    def set_vad_led(self, state):
#        self.write(0x22, [state])
#    def set_volume(self, volume):
#        self.write(0x23, [volume])
#    def change_pattern(self, pattern=None):
#        print('Not support to change pattern')
#    def write(self, cmd, data=[0]):
#        self.dev.ctrl_transfer(
#            usb.util.CTRL_OUT | usb.util.CTRL_TYPE_VENDOR | usb.util.CTRL_RECIPIENT_DEVICE,
#            0, cmd, 0x1C, data, self.TIMEOUT)
#    def close(self):
#        """
#        close the interface
#        """
#        usb.util.dispose_resources(self.dev)

#def find(vid=0x2886, pid=0x0018):
#    dev = usb.core.find(idVendor=vid, idProduct=pid)
#    if not dev:
#        return
#    # configuration = dev.get_active_configuration()
#    # interface_number = None
#    # for interface in configuration:
#    #     interface_number = interface.bInterfaceNumber
#    #     if dev.is_kernel_driver_active(interface_number):
#    #         dev.detach_kernel_driver(interface_number)
#    return PixelRing(dev)

def callback(self, audio):
    print("start recognize")
    try:
        you = rec.recognize_google(audio)
        #you = rec.recognize_sphinx(audio, keyword_entries=[("help", 1.0)])
    except:
        you = ""
    print("finish recognize, your speech is: ", you)
    if "help" in you or "hello" in you:
        print("help or hello detected, start light for several seconds")
        #pixel_ring = find()
        #pixel_ring.set_volume(8)
        for pin in LAMP_PIN_ARR:
            GPIO.output(pin, True)
        #time.sleep(8)
        time.sleep(4)
        for pin in LAMP_PIN_ARR:
            GPIO.output(pin, False)
        #time.sleep(2)
        #pixel_ring.off()

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    for pin in LAMP_PIN_ARR:
        GPIO.setup(pin, GPIO.OUT)
    for i, mic_name in enumerate (sr.Microphone.list_microphone_names()):
        print("mic: " + mic_name)
        # pulse seems better than usb mic
        if "pulse" in mic_name:
        #if "USB PnP Sound Device" in mic_name:
            mic = sr.Microphone(device_index=i, chunk_size=1024, sample_rate=16000)
    rec = sr.Recognizer()
    rec.dynamic_energy_threshold = True
    rec.non_speaking_duration= 0.1
    rec.pause_threshold = 0.1
    rec.energy_threshold = 4000

    with mic as source:
        rec.adjust_for_ambient_noise(source, duration=1)
    # not test
    print("recognize")
    rec.listen_in_background(mic, callback, phrase_time_limit=1)

    # test
    #print("start test")
    #for i in range(10):
    #    with mic as source:
    #        audio = rec.listen(source)
    #    print("write file", i)
    #    with open(str(i)+".flac", "wb") as f:
    #        f.write(audio.get_flac_data())

    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        for pin in LAMP_PIN_ARR:
            GPIO.output(pin, False)
