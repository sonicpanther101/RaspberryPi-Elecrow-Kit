# smart light

import gpiod
import time

pir_pin = 5
led_pin = 6

chip = gpiod.Chip('gpiochip4')
led_line = chip.get_line(led_pin)
pir_line = chip.get_line(pir_pin)

led_line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)
pir_line.request(consumer="Button", type=gpiod.LINE_REQ_DIR_IN)

try:
    while True:
        if pir_line.get_value() == 1:
            led_line.set_value(1)
        else:
            led_line.set_value(0)

finally:
    led_line.release()