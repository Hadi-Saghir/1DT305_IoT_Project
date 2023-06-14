import time
import machine
import network
from secrets import secrets
import ujson
from umqtt.simple import MQTTClient
from umqtt.robust import MQTTClient

print("Running")

# MQTT Topic to publish data from Pico to HiveMQ Cloud
topic_name = "/brewing/check-sound"

# Connect to the WiFi network
print("Connecting to the Wifi")
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(secrets['ssid'], secrets['password'])
while not wifi.isconnected():
    time.sleep(2)
    print("Failed to connect")
    pass
print("Connected to WiFi:", secrets['ssid'])
print("IP address:", wifi.ifconfig()[0])

time.sleep(1)

# MQTT Broker configuration
mqtt_broker = secrets['broker']
mqtt_port = secrets['port']
mqtt_username = secrets['mqtt_username']
mqtt_password = secrets['mqtt_key']

print("Connecting to MQTT Broker: ", mqtt_broker, mqtt_port, mqtt_username, mqtt_password)

# Create MQTT client
client_id = "pico"
client = MQTTClient(client_id, mqtt_broker, port=mqtt_port,
                    user=mqtt_username, password=mqtt_password, ssl=True)

# Connect to MQTT broker
client.connect(clean_session=True)

print("Connecting established")

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
