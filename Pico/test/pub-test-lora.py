from utils.LoRaWANHandler import LoRaWANHandler
from utils.MQTTHandler import MQTTHandler
from secrets import secrets

# Create LoRaWAN and MQTT handlers
lorawan_handler = LoRaWANHandler()
mqtt_handler = MQTTHandler(topics=["test/topic"])

# Connect to LoRaWAN
print("Connecting to LoRaWAN...")
lorawan_handler.connect()
print("LoRaWAN connected successfully!")

# Connect to MQTT broker
print("Connecting to MQTT broker...")
mqtt_handler.connect_to_mqtt()
print("Connected to MQTT broker:", mqtt_handler.broker)

# Send a test message via LoRaWAN
print("Sending a test message via LoRaWAN...")
lorawan_handler.get()
print("Test message sent via LoRaWAN!")

# Publish a test message via MQTT
print("Publishing a test message via MQTT...")
mqtt_handler.publish_message("test/topic", "Hello from MQTT!")
print("Test message published via MQTT!")

# Wait for messages
while True:
    time.sleep(1)
