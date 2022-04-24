#!/bin/python3

import time
import RPi.GPIO as GPIO

LAMP_PIN = [17, 27, 22, 13, 19, 26]

GPIO.setmode(GPIO.BCM)
for pin in LAMP_PIN:
    GPIO.setup(pin, GPIO.OUT)

if __name__ == '__main__':
    try:
        while True:
            for pin in LAMP_PIN:
                GPIO.output(pin, True)
                time.sleep(1)
            print("true")
            time.sleep(10)
            for pin in LAMP_PIN:
                GPIO.output(pin, False)
                time.sleep(1)
            print("false")
            time.sleep(2)
    except KeyboardInterrupt:
            for pin in LAMP_PIN:
                GPIO.output(pin, False)
                time.sleep(1)
