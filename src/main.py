import time
import machine
import network
from secrets import secrets
import ujson
from umqtt.simple import MQTTClient


# MQTT Topic to publish data from Pico to HiveMQ Cloud
topic_name = "/testsensor"

# Connect to the WiFi network
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(secrets['ssid'], secrets['password'])
while not wifi.isconnected():
    pass
print("Connected to WiFi:", secrets['ssid'])
print("IP address:", wifi.ifconfig()[0])

# MQTT Broker configuration
mqtt_broker = secrets['broker']
mqtt_port = secrets['port']
mqtt_username = secrets['mqtt_username'].encode('utf-8')
mqtt_password = secrets['mqtt_key'].encode('utf-8')

# Create MQTT client
client_id = "pico"
client = MQTTClient(client_id, mqtt_broker, port=mqtt_port,
                    user=mqtt_username, password=mqtt_password, keepalive=3600)

# Connect to MQTT broker
client.connect(clean_session=True)

# Define MQTT callback function


def publish_callback(topic, msg):
    print("Published: ", topic, msg)


# Continuously measure the distance and send the value to HiveMQ
print("Starting the distance measurement")
while True:
    try:
        message = ujson.dumps({"value": 1})
        client.publish(topic_name, message, callback=publish_callback)
    except Exception as e:
        print("Distance measurement failure:", e)
    time.sleep(1)
