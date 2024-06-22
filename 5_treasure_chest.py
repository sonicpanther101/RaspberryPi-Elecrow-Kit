# doorbell

import gpiod
import time

hall_pin = 4
green_pin = 5
red_pin = 6

chip = gpiod.Chip('gpiochip4')

hall_line = chip.get_line(hall_pin)
green_line = chip.get_line(green_pin)
red_line = chip.get_line(red_pin)

green_line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)
red_line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)
hall_line.request(consumer="Button", type=gpiod.LINE_REQ_DIR_IN)

try:
    while True:
        if hall_line.get_value() == 1:
            red_line.set_value(1)
            green_line.set_value(1)
            time.sleep(0.5)
            red_line.set_value(0)
            green_line.set_value(0)
            time.sleep(0.5)
        else:
            red_line.set_value(0)
            green_line.set_value(0)
finally:
    red_line.release()
    green_line.release()
    hall_line.release()