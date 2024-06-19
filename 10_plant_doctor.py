# plant doctor

import spidev
import time
import sys
import gpiod

chip = gpiod.Chip('gpiochip4')
buzzer_pin = 5
led_pin = 6
led_line = chip.get_line(led_pin)
buzzer_line = chip.get_line(buzzer_pin)


spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1000000


def readadc(adcnum):
	r = spi.xfer2([1,8+adcnum<<4,0])
	adcout = ((r[1]&3)<<8)+r[2]
	return adcout
try:
        while True:
            value = readadc(0)
            if(value<300):
                buzzer_pin.set_value(1)
                led_pin.set_value(0)
            else:
                buzzer_pin.set_value(0)
                led_pin.set_value(1)

finally:
    led_line.release()
    buzzer_line.release()
