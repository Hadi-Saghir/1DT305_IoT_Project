import network
import time
from umqtt.simple import MQTTClient
from secrets import secrets


class MQTTHandler:
    def __init__(self, topics):
        self.broker = secrets['mqtt_broker']
        self.port = secrets['mqtt_port']
        self.username = secrets['mqtt_username']
        self.password = secrets['mqtt_key']
        self.client_id = "pico"
        self.client = MQTTClient(client_id="test",
                                 server=secrets['mqtt_broker'],
                                 port=secrets['mqtt_port'],
                                 user=secrets['mqtt_username'],
                                 password=secrets['mqtt_key'],
                                 keepalive=secrets['mqtt_keepalive']
                                 #,ssl=True,
                                 #ssl_params=secrets['mqtt_ssl_params']
                                 )
        self.topics = topics
        self.message_handler = None

    def publish_callback(self, topic, msg):
        print("Published:", topic, msg)

    def publish_message(self, topic, message, qos=0):
        try:
            result = self.client.publish(topic, message, qos)
            if result[0] == MQTTClient.MQTT_MSG_PUBACK:
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
