# https://dronebotworkshop.com/raspberry-pi-gpio/
from gpiozero import Button
from subprocess import check_call
from signal import pause

def shutdown():
    check_call(['sudo', 'poweroff'])

shutdown_btn = Button(5, hold_time=2)
shutdown_btn.when_held = shutdown

pause()