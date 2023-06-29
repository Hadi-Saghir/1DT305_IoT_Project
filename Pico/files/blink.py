from machine import Pin
from utime import sleep

led = Pin("LED", Pin.OUT) #GPIO2/D4
for n in range(1,3):
    led.value(1) #on
    sleep(3)
    led.value(0) #off
    sleep(3)