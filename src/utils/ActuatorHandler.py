import time
import machine

class ActuatorHandler:
    def __init__(self):
        # Initialize actuator parameters
        self.led_pin = machine.Pin(2, machine.Pin.OUT)
        self.button_pin = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)

    def simulate_button_press(self):
        if not self.button_pin.value():
            self.led_pin.on()
            print("Coffee machine turned on")
        else:
            self.led_pin.off()
            print("Coffee machine turned off")

    def machine_status(self):
        if self.button_pin.value():
            print("Coffee machine is currently turned off")
        else:
            print("Coffee machine is currently turned on")

    def turn_on_machine(self):
        if self.button_pin.value():
            self.led_pin.on()
            print("Coffee machine turned on")
        else:
            print("Coffee machine is already turned on")

    def turn_off_machine(self):
        if not self.button_pin.value():
            self.led_pin.off()
            print("Coffee machine turned off")
        else:
            print("Coffee machine is already turned off")

    def run(self):
        print("Starting actuator simulation")
        while True:
            self.simulate_button_press()
            time.sleep(0.1)
