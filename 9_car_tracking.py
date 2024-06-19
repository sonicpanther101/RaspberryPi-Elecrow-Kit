# car tracking

import gpiod
import time


chip = gpiod.Chip('gpiochip4')
ir_pin = 4
green_pin = 5
red_pin = 6

ir_line = chip.get_line(ir_pin)
green_line = chip.get_line(green_pin)
red_line = chip.get_line(red_pin)


try:
    while True:
        if ir_line.get_value() == 1:
            green_line.set_value(1)
            red_line.set_value(0)
            print("on track")

        else:
            green_line.set_value(0)
            red_line.set_value(1)
            print("off track")
finally:
    ir_line.release()
    green_line.release()
    red_line.release()
