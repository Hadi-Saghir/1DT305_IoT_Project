import time
import re
from secrets import secrets
from utils.WifiConnectionHandler import ConnectionHandler
from utils.MQTTHandler import MQTTHandler
from utils.SensorHandler import SensorHandler
from utils.SensorHandler import Sensor
from utils.ActuatorHandler import ActuatorHandler

class Machine:
    def __init__(self):
        self.connection_handler = ConnectionHandler()
        self.connection_handler.connect_to_wifi()
        self.mqtt_handler = MQTTHandler(["brew/start", "warm/start"])
        self.mqtt_handler.connect_to_mqtt()
        self.sensor_handler = SensorHandler()
        self.actuator_handler = ActuatorHandler()

        #Energy variables
        self.command_counter = 0
        self.command_received = False

        #LoRaWan
        #self.lora = LoRaCon()
        #self.lora.connect()
        
        

    def handle_message(self, topic, message):
        if topic == b'brew/start' and not self.brew_started:
            self.brew_started = True
            self.mqtt_handler.publish_message("brew/started", "Brew process started")
            if not self.sensor_handler.isCoffeeOn():
                self.actuator_handler.flash_led()
            self.brewing()

        elif topic == b'warm/start':
            duration = message.decode().strip("\n\r\t ")
            if self.validate_duration(duration):
                self.mqtt_handler.publish_message("warm/started", "Warm process started")
                self.run_warm_process(duration)
            else:
                print("Invalid duration format. Expected format: MM:SS")
        self.command_counter = 0
        self.command_received = True

    def validate_duration(self, duration):
        pattern = r"^\d\d:\d\d$" 
        return re.match(pattern, duration) is not None

    def run_warm_process(self, duration):
        duration_minutes = int(duration.split(":")[0])
        duration_seconds = int(duration.split(":")[1])
        end_time = time.time() + duration_minutes * 60 + duration_seconds
        
        while time.time() < end_time:
            #Measure data and report to cloud for warm report
            temperature, humidity = self.sensor_handler.read(Sensor.DH11)
            self.mqtt_handler.publish_message("warm/sensor/temp", str(temperature))
            self.mqtt_handler.publish_message("warm/sensor/humid", str(humidity))

            #Turn on coffee machine if off
            if not self.sensor_handler.isCoffeeOn:
                self.actuator_handler.flash_led()

            time.sleep(15)
            
        #Turn off coffee machine
        if self.sensor_handler.isCoffeeOn:
                self.actuator_handler.flash_led()
            
    def brewing(self):
        #Wait for the brewing process
        time.sleep(5)
        
        #Measure data and report to cloud for brew report
        temperature = self.sensor_handler.read(Sensor.DH11)
        self.mqtt_handler.publish_message("brew/done", "Brew process completed")
        self.mqtt_handler.publish_message("brew/done/sensor/temp", str(temperature))
        
        #Turn off coffee machine
        if self.sensor_handler.isCoffeeOn:
                self.actuator_handler.flash_led()
                
    def is_night_time(self):
        current_hour = time.localtime()[3]  #index for hour
        return current_hour >= 20 or current_hour < 8
    

    def enter_deep_sleep(self, duration):
        # Calculate the sleep time in milliseconds
        sleep_time = duration * 60 * 60 * 1000  # Convert hours to milliseconds
        #machine.deepsleep(sleep_time)

    def run(self):
        self.mqtt_handler.set_message_handler(self.handle_message)

        while True:
            if not self.mqtt_handler.isConnected():
                print("Lost connection to MQTT broker. Reconnecting...")
                self.mqtt_handler.connect_to_mqtt()
                self.mqtt_handler.setup_subscriptions()
                time.sleep(1)

            self.mqtt_handler.client.check_msg()

            machine.lightsleep(1000 * 15)
    
            
            # Check if another command has been received
            if self.command_received:
                self.command_counter += 1

                # Wait for 10 loops (15 seconds * 4)
                if self.command_counter >= 4:
                    print("No additional commands received. Entering deep sleep...")
                    # Calculate deep sleep time until 8 AM
                    self.enter_deep_sleep(2) #Duration in hours
                    self.command_counter = 0
                    self.command_received = False
            
            # Check if it's night time, and enter deep sleep if true
            if self.is_night_time():
                self.enter_deep_sleep(2) #Duration in hours

                print(deep_sleep_time)
                self.enter_deep_sleep(deep_sleep_time)


machine = Machine()
machine.run()
