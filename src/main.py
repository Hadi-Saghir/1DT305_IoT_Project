import time
from secrets import secrets
from utils.ConnectionHandler import ConnectionHandler
from utils.MQTTHandler import MQTTHandler
from utils.SensorHandler import SensorHandler
from utils.ActuatorHandler import ActuatorHandler

print("Running")
class Machine:
    def __init__(self):
        self.connection_handler = ConnectionHandler()
        self.connection_handler.connect_to_wifi()
        self.mqtt_handler = MQTTHandler(["/brewing", "/topic2"])
        self.sensor_handler = SensorHandler()
        self.actuator_handler = ActuatorHandler()
        self.state = "off"

    def check_temperatures(self):
        # Check temperatures every 1 minute
        while True:
            self.sensor_handler.read_temperature_humidity()

            if self.state == "off":
                if self.sensor_handler.is_temperature_absurdly_high():
                    self.alertClient()
            
            time.sleep(60)

    def brew_coffee(self):
        while self.state == "brewing":
            self.sensor_handler.read_vibration()
            
            if self.sensor_handler.is_coffee_ready():
                self.state = "warm"
                self.actuator_handler.turn_on_warming_plate()

    def run(self):
        while True:

            self.mqtt_handler.client.check_msg()  # Check for incoming MQTT messages

            if not self.mqtt_handler.isConnected():  # Reconnect if MQTT connection is lost
                print("Lost connection to MQTT broker. Reconnecting...")
                self.mqtt_handler.connect_to_mqtt()
                time.sleep(1)
            
            if self.mqtt_handler.isConnected(): self.mqtt_handler.publish_message('/brewing', 'test')
            if self.state == "off":
                print("temp")
                #self.check_temperatures()
            elif self.state == "brewing":
                self.brew_coffee()
            elif self.state == "warm":
                if self.sensor_handler.is_temperature_low():
                    self.actuator_handler.turn_on_warming_plate()
                else:
                    self.actuator_handler.turn_off_warming_plate()

            time.sleep(5)

    def alertClient(self):
        # Implement alerting the client here
        pass
machine = Machine()
machine.run()
