import struct
import binascii
import time
from lib.LoRaWAN import lora
from secrets import secrets

class LoRaWANHandler:
    def __init__(self):
        self.dev_eui = secrets['lora_dev_eui']
        self.app_eui = secrets['lora_app_eui']
        self.app_key = secrets['lora_app_key']
        self.lora = lora()
        self.connected = False

    def connect(self):
        self.lora.configure(self.dev_eui, self.app_eui, self.app_key)
        self.lora.startJoin()
        print("Start Join.....")
        while not self.lora.checkJoinStatus():
            print("Joining....")
            time.sleep(1)
        self.connected = True
        print("Join success!")

    def get(self):
        if self.connected:
            # Send data
            data = b'Hello, TTN!'
            self.lora.send(data)
            print("Data sent.")

            # Receive data
            recv_data = self.lora.receive()
            print("Received data: ", recv_data)
        else:
            print("Not connected to LoRaWAN network.")

    def check_status(self):
        if self.connected:
            print("Connected to LoRaWAN network.")
        else:
            print("Not connected to LoRaWAN network.")