from machine import ADC, Pin
import time
import dht

class Sensor:
    DH11 = 4
    VIBRATION = 26
    PHOTO_RESISTOR = 27

class SensorHandler:
    def __init__(self):
        self.dh11_pin = Pin(21, Pin.IN)
        self.photo_resistor_pin = ADC(Pin(27))

    def read(self, sensor):
        if sensor == Sensor.DH11:
            d = dht.DHT11(Pin(21))
            d.measure()
            temperature = d.temperature()
            humidity = d.humidity()
            return (temperature, humidity)
        
        elif sensor == Sensor.PHOTO_RESISTOR:
            light = self.photo_resistor_pin.read_u16()
            darkness = round(light / 65535 * 100, 2)
            return darkness
        
    def is_outlier(self, value, threshold_low, threshold_high):
        return value < threshold_low or value > threshold_high

    def isCoffeeOn(self):
        num_values = 10
        num_outliers = 0
        outlier_threshold_low = 1.0
        outlier_threshold_high = 2.5
        
        for _ in range(num_values):
            darkness = self.read(Sensor.PHOTO_RESISTOR)  # Replace with your sensor reading function
            
            if self.is_outlier(darkness, outlier_threshold_low, outlier_threshold_high):
                num_outliers += 1
            
            if num_outliers >= 3:
                break
        
        return num_outliers < 3

# Test photo resistor
while False:
    sens = SensorHandler()
    coffee_on = sens.isCoffeeOn()
    print("Is coffee on?", coffee_on)
    time.sleep(1)


# Test sensors
while False:
    sen = SensorHandler()
    temperature, humidity = sen.read(Sensor.DH11)
    darkness = sen.read(Sensor.PHOTO_RESISTOR)
    
    print("Temperature:", temperature)
    print("Humidity:", humidity)
    print("Darkness:", darkness)
    print()
    
    time.sleep(1)
