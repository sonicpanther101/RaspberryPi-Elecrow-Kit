import spidev
import time
import sys
import gpiod

chip = gpiod.Chip('gpiochip4')
led_pin = 5
led_line = chip.get_line(led_pin)

led_line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)

spi = spidev.SpiDev(0,1)
spi.open(0,0)
spi.max_speed_hz = 1000000

def dimmer(output_line, brightness_percent):
    hz = 1/10000
    
    brightness = brightness_percent/100
    
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
        return x/4/2.56


try:
        while True:
            value = readadc(0)
            brightness = brightness_func(value)
            #print(brightness)
            dimmer(led_line, brightness)
            #time.sleep(0.1)
finally:
    led_line.release()