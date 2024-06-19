import gpiod

led_pin = 5
button_pin = 6

chip = gpiod.Chip('gpiochip4')

led_line = chip.get_line(led_pin)
button_line = chip.get_line(button_pin)

led_line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)
button_line.request(consumer="Button", type=gpiod.LINE_REQ_DIR_IN)

try:
    while True:
        if button_line.get_value() == 1:
            led_line.set_value(1)
        else:
            led_line.set_value(0)
finally:
    led_line.release()
    button_line.release()
