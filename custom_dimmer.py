import gpiod
import time

led_pin  = 5

chip = gpiod.Chip('gpiochip4')

led_line = chip.get_line(led_pin)

led_line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)

def dimmer(output_line, brightness_percent):
    hz = 1/1000
    
    brightness = brightness_percent/100
    
    if brightness != 0:
        output_line.set_value(1)
        time.sleep(hz*brightness)
    if brightness != 1:
        output_line.set_value(0)
        time.sleep(hz*(1-brightness))

try:
    while True:
        dimmer(led_line, 25)
finally:
    led_line.release()
