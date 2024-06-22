# bright and dark

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


def readadc(adcnum):
	r = spi.xfer2([1,8+adcnum<<4,0])
	adcout = ((r[1]&3)<<8)+r[2]
	return adcout
try:
        while True:
            value = readadc(0)
            print(value)
            if(value<900):
                led_line.set_value(1)
            else:
                led_line.set_value(0)

finally:
    led_line.release()
