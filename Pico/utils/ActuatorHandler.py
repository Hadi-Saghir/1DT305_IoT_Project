from machine import Pin
import time

class ActuatorHandler:
    def __init__(self):
        self.led_pin = Pin("LED", Pin.OUT)  # Pico's built-in LED pin

    def flash_led(self):
        for _ in range(3):  # Flash the LED three times
            self.led_pin.on()
            time.sleep(0.5)
            self.led_pin.off()
            time.sleep(0.5)

    def turn_off_led(self):
        self.led_pin.off()
        