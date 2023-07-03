import time
import json
import re
from secrets import secrets
from utils.WiFiConnectionHandler import ConnectionHandler
#from utils.LoRaConnectionHandler import LoRaConnectionHandler
from utils.MQTTHandler import MQTTHandler
from utils.SensorHandler import SensorHandler
from utils.SensorHandler import Sensor
from utils.ActuatorHandler import ActuatorHandler

class Machine:
    def __init__(self):
        self.connection_handler = ConnectionHandler()
        self.connection_handler.connect()
        self.mqtt_handler = MQTTHandler(["brew/start", "warm/start"])
        self.mqtt_handler.connect_to_mqtt()
        self.sensor_handler = SensorHandler()
        self.actuator_handler = ActuatorHandler()

        #Energy variables
        self.command_counter = 0
        self.command_received = False

        #LoRaWan
        #self.lora = LoRaConnectionHandler()
        #self.lora.connect()
        
        

    def handle_message(self, topic, message):
        if topic == b'brew/start':
            self.mqtt_handler.publish_message(b'brew/started', "Brew process started")
            self.brewing()

        elif topic == b'warm/start':
            data = json.loads(message.decode())
            duration = data["content"].strip()
            print(duration)
            if self.validate_duration(duration):
                self.mqtt_handler.publish_message("warm/started", "Warm process started")
                self.run_warm_process(duration)
            else:
                print("Invalid duration format. Expected format: HH:MM")
        self.command_counter = 0
        self.command_received = True

    def validate_duration(self, duration):
        pattern = r"^\d\d:\d\d$" 
        return re.match(pattern, duration) is not None

    def run_warm_process(self, duration):
        duration_minutes, duration_seconds = duration.split(":")
        duration_minutes = int(duration_minutes)
        duration_seconds = int(duration_seconds)
        end_time = time.time() + duration_minutes * 60 + duration_seconds
        
        while time.time() < end_time:
            #Measure data and report to cloud for warm report
            temperature, humidity = self.sensor_handler.read(Sensor.DH11)
            #self.lora.pub_sensor_values("w", temperature, humidity)
            self.mqtt_handler.publish_message(b'warm/sensor/temp', str(temperature))
            self.mqtt_handler.publish_message(b'warm/sensor/humid', str(humidity))

            #Turn on coffee machine if on
            if not self.sensor_handler.isCoffeeOn():
                print("Coffee machine turning on")
                self.actuator_handler.flash_led()

            time.sleep(15)
            
        #Turn off coffee machine
        if self.sensor_handler.isCoffeeOn():
            print("Coffee machine turning off")
            self.actuator_handler.flash_led()
            
    def brewing(self):
        #Turn on coffee machine
        if not self.sensor_handler.isCoffeeOn():
            print("Coffee machine turning on")
            self.actuator_handler.flash_led()
                
        #Wait for the brewing process
        time.sleep(15)
        
        #Measure data and report to cloud for brew report
        temperature, humidity = self.sensor_handler.read(Sensor.DH11)
        #self.lora.pub_sensor_values("b", temperature, humidity)
        self.mqtt_handler.publish_message(b'brew/done', "Brew process completed")
        self.mqtt_handler.publish_message(b'brew/done/sensor/temp', str(temperature))
        
        #Turn off coffee machine
        if self.sensor_handler.isCoffeeOn():
            print("Coffee machine turning off")
            self.actuator_handler.flash_led()
                
    def is_night_time(self):
        current_hour = time.localtime()[3]  #index for hour
        return current_hour >= 20 or current_hour < 8
    

    def enter_deep_sleep(self, duration):
        sleep_time = duration * 60 * 60 * 1000 # convert to ms
        #machine.deepsleep(sleep_time) #Commeted out for presentation and development (cancels the run)
        time.sleep(5)

    def run(self):
        self.mqtt_handler.set_message_handler(self.handle_message) 

        while True:
            if not self.mqtt_handler.isConnected():
                print("Lost connection to MQTT broker. Reconnecting...")
                self.mqtt_handler.connect_to_mqtt()
                self.mqtt_handler.setup_subscriptions()
                time.sleep(15)

            self.mqtt_handler.client.check_msg()
            
            # Check if another command has been received
            if self.command_received:
                self.command_counter += 1

                # Wait for 10 loops (15 seconds * 4)
                if self.command_counter >= 4:
                    print("No additional commands received. Entering deep sleep...")
                    self.command_counter = 0
                    self.command_received = False
                    self.enter_deep_sleep(2) #Duration in hours
            
            # Check if it's night time, and enter deep sleep if true
            elif self.is_night_time():
                self.enter_deep_sleep(10) #Duration in hours
            
            else:
                self.enter_deep_sleep(0.2) #Duration in hours


machine = Machine()
machine.mqtt_handler.client.check_msg()
machine.run()
