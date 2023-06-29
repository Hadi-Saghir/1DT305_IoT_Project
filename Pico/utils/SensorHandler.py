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
        self.vibration_pin = Pin(26, Pin.IN)
        self.photo_resistor_pin = ADC(Pin(27))

    def read(self, sensor):
        if sensor == Sensor.DH11:
            d = dht.DHT11(Pin(21))
            d.measure()
            temperature = d.temperature()
            humidity = d.humidity()
            return (temperature, humidity)
        
        elif sensor == Sensor.VIBRATION:
            vibration_state = self.vibration_pin.value()
            return vibration_state
        
        elif sensor == Sensor.PHOTO_RESISTOR:
            light = self.photo_resistor_pin.read_u16()
            darkness = round(light / 65535 * 100, 2)
            return darkness
        
    def isCoffeeOn():
        num_readings = 6
        threshold_low = 1.0
        threshold_high = 2.5
        readings = []
        outlier_ignored = False
        
        for _ in range(num_readings):
            darkness = self.sen.read(Sensor.PHOTO_RESISTOR)
            
            # Ignore outlier once every num_readings readings
            if not outlier_ignored and (darkness < threshold_low or darkness > threshold_high):
                outlier_ignored = True
                continue
            
            readings.append(darkness)
            
            if len(readings) == num_readings:
                average = sum(readings) / num_readings
                
                return threshold_low <= average <= threshold_high       



while False:
    sen = SensorHandler()
    temperature, humidity = sen.read(Sensor.DH11)
    vibration = sen.read(Sensor.VIBRATION)
    darkness = sen.read(Sensor.PHOTO_RESISTOR)
    
    print("Temperature:", temperature)
    print("Humidity:", humidity)
    print("Vibration:", vibration)
    if vibration == 1:
        print("No vibration...")
    else:
        print("Vibration detected...")
    print("Darkness:", darkness)
    print()
    
    time.sleep(1)
