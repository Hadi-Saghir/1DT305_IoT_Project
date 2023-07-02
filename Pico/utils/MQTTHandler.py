import network
import time
from umqtt.simple import MQTTClient
from secrets import secrets


class MQTTHandler:
    def __init__(self, topics):
        self.broker = secrets['MQTT_BROKER']
        self.port = secrets['MQTT_PORT']
        self.username = secrets['MQTT_USERNAME']
        self.password = secrets['MQTT_KEY']
        self.client_id = "pico"
        self.client = MQTTClient(client_id=self.client_id,
                                 server=self.broker,
                                 port=self.port,
                                 user=self.username,
                                 password=self.password,
                                 keepalive=secrets['MQTT_KEEPALIVE']
                                 #,ssl=True,
                                 #ssl_params=secrets['MQTT_SSL_PARAM']
                                 )
        self.topics = topics
        self.message_handler = None

    def publish_callback(self, topic, msg):
        print("Published:", topic, msg)

    def publish_message(self, topic, message, qos=0):
        try:
            result = self.client.publish(topic, message, qos)
            print("Published successfully:", topic, message)
        except Exception as e:
            print("Publishing message failure:", e)


    def setup_subscriptions(self):
        for topic in self.topics:
            self.client.set_callback(self.receive_callback)
            self.client.subscribe(topic)

    def receive_callback(self, topic, msg):
        print("Received message on topic:", topic)
        print("Message:", msg)
        if self.message_handler is not None:
            self.message_handler(topic, msg)

    def connect_to_mqtt(self):
        try:
            self.client.connect(clean_session=True)
            print("Connected to MQTT broker:", self.broker)
            self.setup_subscriptions()
        except Exception as e:
            print("MQTT connection failure:", e)
            raise Exception("MQTT connection failure:")

    def isConnected(self):
        try:
            self.client.ping()
            return True
        except OSError:
            return False

    def set_message_handler(self, handler):
        self.message_handler = handler
