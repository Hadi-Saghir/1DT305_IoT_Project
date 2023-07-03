from machine import Pin
import time

class ActuatorHandler:
    def __init__(self):
        self.red_pin = Pin(11, Pin.OUT)   # Pin 13 for red
        self.green_pin = Pin(12, Pin.OUT) # Pin 12 for green
        self.blue_pin = Pin(13, Pin.OUT)  # Pin 11 for blue

    def flash_led(self):
        self.flash_red()
        self.flash_green()
        self.flash_blue()

    def flash_red(self):
        self.red_pin.on()
        time.sleep(0.5)
        self.red_pin.off()

    def flash_green(self):
        self.green_pin.on()
        time.sleep(0.5)
        self.green_pin.off()

    def flash_blue(self):
        self.blue_pin.on()
        time.sleep(0.5)
        self.blue_pin.off()

    def turn_off_led(self):
        self.red_pin.off()
        self.green_pin.off()
        self.blue_pin.off()

# Test
while False:
    actuator = ActuatorHandler()

    print("Testing flash_red()")
    actuator.flash_red()
    time.sleep(1)

    print("Testing flash_green()")
    actuator.flash_green()
    time.sleep(1)

    print("Testing flash_blue()")
    actuator.flash_blue()
    time.sleep(1)

    print("Testing flash_led()")
    actuator.flash_led()
    time.sleep(1)

    actuator.turn_off_led()

