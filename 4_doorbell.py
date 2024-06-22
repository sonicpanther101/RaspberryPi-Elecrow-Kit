# doorbell

import gpiod
import time

touch_pin = 5
buzzer_pin = 6

chip = gpiod.Chip('gpiochip4')

buzzer_line = chip.get_line(buzzer_pin)
touch_line = chip.get_line(touch_pin)

buzzer_line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)
touch_line.request(consumer="Button", type=gpiod.LINE_REQ_DIR_IN)

try:
    while True:
        if touch_line.get_value() == 1:
            buzzer_line.set_value(1)
            time.sleep(3)
        else:
            buzzer_line.set_value(0)
finally:
    touch_line.release()
    buzzer_line.release()