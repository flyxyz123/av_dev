#!/bin/python3

import time
import RPi.GPIO as GPIO

PIN_ARR = [23, 24]

GPIO.setmode(GPIO.BCM)
for pin in PIN_ARR:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

print(PIN_ARR[0])
print(PIN_ARR[1])

if __name__ == '__main__':
    try:
        while True:
            print("arr [0] true, [1] false")
            GPIO.output(PIN_ARR[0], True)
            GPIO.output(PIN_ARR[1], False)
            time.sleep(2)
            print("false")
            GPIO.output(PIN_ARR[0], False)
            GPIO.output(PIN_ARR[1], False)
            time.sleep(2)
            print("arr [0] false, [1] true")
            GPIO.output(PIN_ARR[0], False)
            GPIO.output(PIN_ARR[1], True)
            time.sleep(2)
    except KeyboardInterrupt:
            print("false")
            GPIO.output(PIN_ARR[0], False)
            GPIO.output(PIN_ARR[1], False)
