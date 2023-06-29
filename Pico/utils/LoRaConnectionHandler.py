import json
import socket
import struct
from network import LoRa
import time
import _thread
from secrets import secrets

class LoRaConnectionHandler:
    def __init__(self):
        self.lora = None
        self.lora_sock = None
    
    def connect(self):
        self.lora.configure(secrets["LORA_DEV_EUI"], secrets["LORA_APP_EUI"], secrets["LORA_APP_KEY"])
        self.lora = LoRa(mode=LoRa.LORA, rx_iq=True, region=LoRa.EU868)
        self.lora_sock = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
        self.lora_sock.setblocking(False)
        self.lora.configure(secrets["LORA_DEV_EUI"], secrets["LORA_APP_EUI"], secrets["LORA_APP_KEY"])
        self.lora.startJoin()
        max_tries = 3 #Helium costs money to send join requests
        for _ in range(max_tries):
            if self.lora.has_joined():
                break;
            time.sleep(3)
            print('Not yet joined...')
        else:
            raise Exception("Failed to join LoRa modules after multiple tries.")

        print('LoRa connected')
             
        
        
    def pub_sensor_values(self, client, topic, temperature, humidity):
        # Create the message dictionary
        message = {
            "temperature": "{{temperature}}",
            "humidity": "{{humidity}}"
        }''

        # Fill in the dynamic values in the message template
        message["temperature"] = temperature
        message["humidity"] = humidity

        # Convert the message to JSON
        json_message = json.dumps(message)

        # Send the JSON message using your desired method
        # For example, you can publish it to an MQTT topic
        try:
            client.publish(topic=topic, msg=json_message)
        except Exception as e:
            print("publish failed")
             # if WLAN.isConnected() use wifi

             
