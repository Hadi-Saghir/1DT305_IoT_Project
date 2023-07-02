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
        temperature = ...
        humidity = ...
        
        """
        Prepare data packing to send
        Payload format is: >hB where
        h = Temperature         (2 bytes, 16 bits, signed)       Range: -32,768 to 32,767
        B = Humidity            (1 byte,  8 bits,  unsigned)     Range: 0 to 255
        """
        package = struct.pack('>hB', int(temperature), int(humidity))
        s.send(package) 
        print('Sensor data sent!') 

             
