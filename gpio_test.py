#!/bin/python3

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

if __name__ == '__main__':
    try:
        while True:
            GPIO.output(17, True)
            GPIO.output(27, True)
            GPIO.output(22, True)
            GPIO.output(5, True)
            GPIO.output(6, True)
            GPIO.output(26, True)
            print("true")
            time.sleep(4)
            GPIO.output(17, False)
            GPIO.output(27, False)
            GPIO.output(22, False)
            GPIO.output(5, False)
            GPIO.output(6, False)
            GPIO.output(26, False)
            print("false")
            time.sleep(4)
    except KeyboardInterrupt:
            GPIO.output(17, False)
            GPIO.output(27, False)
            GPIO.output(22, False)
            GPIO.output(5, False)
            GPIO.output(6, False)
            GPIO.output(26, False)
