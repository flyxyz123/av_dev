#!/bin/python3

import time
import RPi.GPIO as GPIO

MYPIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(MYPIN, GPIO.OUT)


if __name__ == '__main__':
    try:
        while True:
            GPIO.output(MYPIN, True)
            print("true")
            time.sleep(8)
            GPIO.output(MYPIN, False)
            print("false")
            time.sleep(2)
    except KeyboardInterrupt:
            GPIO.output(MYPIN, False)
