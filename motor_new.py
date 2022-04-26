#!/bin/python3
# edited from https://github.com/Freenove/Freenove_4WD_Smart_Car_Kit_for_Raspberry_Pi
# by Daniel, not me

import time
import RPi.GPIO as GPIO

#define pins
SPI_CS_1_PIN = 16 # front right all CS pins are inverted (false=active, ture=deactive)
SPI_CS_2_PIN = 13 # front left
#SPI_CS_3_PIN = 19 # rear right
#SPI_CS_4_PIN = 26 # rear left
SPI_CLK_PIN = 21
#SPI_SDISDO_PIN = 20
SPI_SDISDO_PIN = 7
XSISTR_REVERSE_1_PIN = 12 # front right
XSISTR_REVERSE_2_PIN = 6  # front left
#XSISTR_REVERSE_3_PIN = 5 # rear right
#XSISTR_REVERSE_4_PIN = 6 # rear left

class Motor:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(SPI_CS_1_PIN, GPIO.OUT)
        GPIO.setup(SPI_CS_2_PIN, GPIO.OUT)
        #GPIO.setup(SPI_CS_3_PIN, GPIO.OUT)
        #GPIO.setup(SPI_CS_4_PIN, GPIO.OUT)
        GPIO.setup(SPI_CLK_PIN, GPIO.OUT)
        GPIO.setup(SPI_SDISDO_PIN, GPIO.OUT)
        GPIO.setup(XSISTR_REVERSE_1_PIN, GPIO.OUT)
        GPIO.setup(XSISTR_REVERSE_2_PIN, GPIO.OUT)
        #GPIO.setup(XSISTR_REVERSE_3_PIN, GPIO.OUT)
        #GPIO.setup(XSISTR_REVERSE_4_PIN, GPIO.OUT)
        
    def speed_range(self,speed1,speed2,speed3,speed4):
        if speed1>127:
            speed1=127
        elif speed1<0:
            speed1=0
        
        if speed2>127:
            speed2=127
        elif speed2<0:
            speed2=0
            
        if speed3>127:
            speed3=127
        elif speed3<0:
            speed3=0
            
        if speed4>127:
            speed4=127
        elif speed4<0:
            speed4=0
        return speed1,speed2,speed3,speed4
            
    def set_speed(self, CS, RS, isReverse, value):
        # is reversing or not
        if isReverse:
            GPIO.output(RS, True)
        else:
            GPIO.output(RS, False)
        GPIO.output(CS, True)
        
        # pre-data-sending setup
        bits = '{0:016b}'.format(value)
        GPIO.output(SPI_CLK_PIN, False)
        GPIO.output(CS, False)
        
        # send data
        for x in range(0,16):
            # send one bit
            GPIO.output(SPI_SDISDO_PIN, int(bits[x]))
            # toggle clock
            GPIO.output(SPI_CLK_PIN, True)
            GPIO.output(SPI_CLK_PIN, False)
            
        # deactivate CS after finishing sending bits
        GPIO.output(CS, True)
        
    def setMotorModel(self,speed1,isReverse1,speed2,isReverse2,
                           speed3,isReverse3,speed4,isReverse4):
        speed1,speed2,speed3,speed4=self.speed_range(speed1,speed2,speed3,speed4)
        self.set_speed(SPI_CS_1_PIN, XSISTR_REVERSE_1_PIN, isReverse1, speed1)
        self.set_speed(SPI_CS_2_PIN, XSISTR_REVERSE_2_PIN, isReverse2, speed2)
        #self.set_speed(SPI_CS_3_PIN, XSISTR_REVERSE_3_PIN, isReverse1, speed3)
        #self.set_speed(SPI_CS_4_PIN, XSISTR_REVERSE_4_PIN, isReverse1, speed4)
            
            
motor=Motor()
def loop():
    while True:
        print ('forward')
        #for level in range(40,50):
        for level in range(0,127):
            motor.setMotorModel(level,0,level,0,level,0,level,0)    #Forward
            print(level)
            time.sleep(0.2)
        print("stop")
        motor.setMotorModel(0,0,0,0,0,0,0,0)    #Stop
        print("sleep")
        time.sleep(5)
        print("backward")
        #for level in range(15,25):
        for level in range(0,127):
            motor.setMotorModel(level,1,level,1,level,1,level,1)    #Backward
            print(level)
            time.sleep(0.2)
        print("stop")
        motor.setMotorModel(0,0,0,0,0,0,0,0)    #Stop
        print("sleep")
        time.sleep(2)
    
def destroy():
    motor.setMotorModel(0,0,0,0,0,0,0,0)     
                 
if __name__=='__main__':
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
