#!/bin/python3

import time
import RPi.GPIO as GPIO

MYPIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(MYPIN, GPIO.OUT)

while True:
    GPIO.output(MYPIN, True)
    print("true")
    time.sleep(3)
    GPIO.output(MYPIN, False)
    print("false")
    time.sleep(3)
