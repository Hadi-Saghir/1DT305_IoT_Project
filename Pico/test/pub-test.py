import network
from umqtt.simple import MQTTClient
from secrets import secrets

def test_mqtt_publish():
    # Connect to Wi-Fi
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(secrets['wifi_ssid'], secrets['wifi_password'])
    while not wlan.isconnected():
        pass

    print("Connected to Wi-Fi:", wlan.ifconfig())

    # Connect to MQTT broker
    client = MQTTClient(client_id="test",
                   server=secrets['mqtt_broker'],
                   port=secrets['mqtt_port'],
                   user=secrets['mqtt_username'],
                   password=secrets['mqtt_key'],
                   keepalive=secrets['mqtt_keepalive'],
                   ssl=True,
                   ssl_params=secrets['mqtt_ssl_params'])
    client.connect(clean_session=True)

    print("Connected to MQTT broker:", secrets['mqtt_broker'])
    
    # Define callback function for received messages
    def on_message(topic, message):
        print("Received message on topic:", topic)
        print("Message:", message)

    # Set callback function for received messages
    client.set_callback(on_message)

    # Subscribe to topic
    client.subscribe("test/#")

    client.publish("test/clientId", "the payload2", 2)

    print("Published message to topic")

    # Wait for messages
    try:
        while True:
            client.check_msg()
    finally:
        # Clean up and disconnect from MQTT broker
        client.disconnect()
    
    print("Disconnected from MQTT broker")

def mqtt_reconnect():
    print('Could not connect to MQTT broker, reconnecting: ' + str(client.conn_issue))
    client.reconnect()
    client.publish(last_will_topic, 'Connected', retain=True)

    try:
        client = client.connect()
        print('MQTT Connected')
    except OSError as e:
        print('Error connecting to MQTT, retrying...')
        mqtt_reconnect()

test_mqtt_publish()
