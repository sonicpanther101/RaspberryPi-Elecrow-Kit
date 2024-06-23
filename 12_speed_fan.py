import spidev
import time
import sys
import gpiod

chip = gpiod.Chip('gpiochip4')
motor_pin = 5
motor_line = chip.get_line(motor_pin)

motor_line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1000000

def dimmer(output_line, brightness_percent):
    hz = 1/10000
    
    brightness = brightness_percent/100
    
    brightness =0
    
    if brightness != 0:
        output_line.set_value(1)
        time.sleep(hz*brightness)
    if brightness != 1:
        output_line.set_value(0)
        time.sleep(hz*(1-brightness))

def readadc(adcnum):
	r = spi.xfer2([1,8+adcnum<<4,0])
	adcout = ((r[1]&3)<<8)+r[2]
	return adcout

def brightness_func(x):
        return x/10.23

try:
        while True:
            value = readadc(0)
            brightness = brightness_func(value)
            dimmer(motor_line, brightness)

finally:
    motor_line.release()