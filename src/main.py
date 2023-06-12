import machine
import secrets
from umqtt.robust import MQTTClient

# Pin configuration
sound_pin = machine.Pin(27, machine.Pin.IN)

# MQTT Broker configuration
mqtt_broker = "07bd001441864fcabc7b1a8b9677149a.s2.eu.hivemq.cloud"
mqtt_port = 8883
mqtt_topic = "brewing/check-sound"

# MQTT client configuration
client_id = 'pico'
client_username = secrets.MQTT_USERNAME.encode('utf-8')
client_password = secrets.MQTT_PASSWORD.encode('utf-8')

def check_sound():
    # Check if sound is detected
    sound_detected = sound_pin.value()
    return "true" if sound_detected else "false"

def handle_message(topic, message):
    print("Received message: ", message.decode())
    if topic == mqtt_topic and message.decode() == "check":
        response = check_sound()
        client.publish(topic + "/response", response)

client = MQTTClient(client_id, mqtt_broker, port=mqtt_port, user=client_username, password=client_password, ssl=True)

# Connect to MQTT broker
client.connect()

# Subscribe to MQTT topic
client.set_callback(handle_message)
client.subscribe(mqtt_topic)

# Main loop
while True:
    client.wait_msg()
