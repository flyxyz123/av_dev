#!/bin/python3

import time
import RPi.GPIO as GPIO

# front, right, left, top, back, brake
PIN_ARR = [17, 27, 22, 10, 11, 9]

GPIO.setmode(GPIO.BCM)
for pin in PIN_ARR:
    GPIO.setup(pin, GPIO.OUT)

if __name__ == '__main__':
    try:
        while True:
            print("true")
            for pin in PIN_ARR:
                print("pin", pin)
                GPIO.output(pin, True)
                #time.sleep(1)
            time.sleep(10)
            print("false")
            for pin in PIN_ARR:
                print("pin", pin)
                GPIO.output(pin, False)
                #time.sleep(1)
            time.sleep(2)
    except KeyboardInterrupt:
            print("false")
            for pin in PIN_ARR:
                print("pin", pin)
                GPIO.output(pin, False)
                #time.sleep(1)
