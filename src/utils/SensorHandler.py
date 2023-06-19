import time
import machine
import dht

class SensorHandler:
    def __init__(self):
        # Initialize sensor parameters
        self.dht_sensor = dht.DHT11(machine.Pin(26))
        self.vibration_pin = machine.Pin(14, machine.Pin.IN)
        self.warming_plate_pin = machine.Pin(2, machine.Pin.OUT)

    def read_temperature_humidity(self):
        self.dht_sensor.measure()
        temperature = self.dht_sensor.temperature()
        humidity = self.dht_sensor.humidity()
        print("Temperature:", temperature)
        print("Humidity:", humidity)
        if temperature < 60:
            print("Coffee is getting cold. Turn on warming plate.")
            self.warming_plate_pin.on()
        else:
            self.warming_plate_pin.off()

    def read_vibration(self):
        vibration = self.vibration_pin.value()
        if vibration:
            print("Vibrations detected")
        else:
            print("No vibrations detected")
            print("Coffee is ready")

    def run(self):
        print("Starting sensor data collection")
        for _ in range(240):  # Run for 2 hours (30 seconds * 240)
            self.read_temperature_humidity()
            self.read_vibration()
            time.sleep(30)
        print("Sensor data collection completed")
