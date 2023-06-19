import network
import time
from umqtt.simple import MQTTClient
from secrets import secrets

class MQTTHandler:
    def __init__(self, topics):
        self.broker = secrets['broker']
        self.port = secrets['port']
        self.username = secrets['mqtt_username']
        self.password = secrets['mqtt_key']
        self.client_id = "pico"
        self.client = MQTTClient(self.client_id, self.broker, port=self.port,
                                 user=self.username, password=self.password, ssl=True)
        self.client.connect(clean_session=True)
        self.topics = topics
        self.setup_subscriptions()

    def publish_callback(self, topic, msg):
        print("Published:", topic, msg)

    def publish_message(self, topic, message):
        try:
            result = self.client.publish(topic, message,qos=1)
            if result is not None and result[0] == 0:
                print("Published successfully:", topic, message)
            else:
                print("Failed to publish message:", result)
        except Exception as e:
            print("Publishing message failure:", e)

    def setup_subscriptions(self):
        for topic in self.topics:
            self.client.set_callback(self.receive_callback)
            self.client.subscribe(topic)

    def receive_callback(self, topic, msg):
        print("Received message on topic:", topic)
        print("Message:", msg)
        # Handle received message here
        
    def connect_to_mqtt(self):
        try:
            self.client.connect(clean_session=True)
            self.setup_subscriptions()
            print("Connected to MQTT broker:", self.broker)
        except Exception as e:
            print("MQTT connection failure:", e)
            
    def isConnected(self):
        try:
            self.client.ping()
            return True
        except OSError:
            return False
