# collision alert

import gpiod
import time


chip = gpiod.Chip('gpiochip4')
collision_pin = 4
buzzer_pin = 5
led_pin = 6

collision_line = chip.get_line(collision_pin)
buzzer_line = chip.get_line(buzzer_pin)
led_line = chip.get_line(led_pin)

try:
    while True:
        if collision_line.get_value() == 0:
            buzzer_line.set_value(1)
            led_line.set_value(1)
            time.sleep(0.5)
            buzzer_line.set_value(0)
            led_line.set_value(0)
            time.sleep(0.5)
        else:
            buzzer_line.set_value(0)
            led_line.set_value(0)

finally:
    led_line.release()
    buzzer_line.release()
    collision_line.release()