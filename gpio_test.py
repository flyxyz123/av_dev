#!/bin/python3

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)

while True:
    GPIO.output(2, True)
    print("true")
    time.sleep(3)
    GPIO.output(2, False)
    print("false")
    time.sleep(3)
