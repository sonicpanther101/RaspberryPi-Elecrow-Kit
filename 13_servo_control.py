#!/usr/bin/python
# -*- coding: utf-8 -*-
# Servo control
# author: Tony
# http://elecrow.com/

import gpiod
import time

servo_pin = 5
servo_line=""
fpwm = 50

''' The a and b variables reflect the relationship
    between the duty cycle and the rotation angle. They
    must match the type of servo you are using.
'''
a = 45
b = 18.0

def dimmer(output_line, brightness_percent):
    hz = 1/80
    
    brightness = brightness_percent/100
    
    brightness =0
    
    if brightness != 0:
        output_line.set_value(1)
        time.sleep(hz*brightness)
    if brightness != 1:
        output_line.set_value(0)
        time.sleep(hz*(1-brightness))

def setup():
    global pwm, servo_line
    chip = gpiod.Chip('gpiochip4')
    servo_line = chip.get_line(servo_pin)
    servo_line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)

def setDirection(direction):
    duty = (direction + a)/b
    dimmer(servo_line,duty)
    print("direction =", direction, "-> duty =", duty)
    #time.sleep(1) 
   
print("starting")
setup()
for direction in range(0, 181, 1):
    setDirection(direction)    
setDirection(0)    
servo_line.release() 
print("done")
    
