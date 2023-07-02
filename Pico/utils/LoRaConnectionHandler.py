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

    def check_connection(self):
        if not self.lora.has_joined():
            print("LoRa connection lost. Reconnecting...")
            self.connect()
            return True
        
        
    def pub_sensor_values(self, state, temperature, humidity):
        state = state
        temperature = temperature
        humidity = humidity

        """
        Prepare data packing to send
        Payload format is: >hBc where
        h = Temperature         (2 bytes, 16 bits, signed)       Range: -32,768 to 32,767
        B = Humidity            (1 byte,  8 bits,  unsigned)     Range: 0 to 255
        c = State               (1 byte,  8 bits,  character)     Values: 'w' or 'b'
        
        """
        max_tries = 3

        for _ in range(max_tries):
            try:
                if not self.lora.has_joined():
                    self.connect()
                
                package = struct.pack('>hBc', int(temperature), int(humidity), state.encode())
                self.lora_sock.send(package)
                print('Sensor data sent!')
                break
    
            except Exception as e:
                print('Error:', e)
                time.sleep(15)
    
        else:
            try:
                self.lora_sock.close()
                self.lora = None
                self.lora_sock = None
                wifi_connection_handler = WiFiConnectionHandler()
                wifi_connection_handler.connect()
                wifi_connection_handler.pub_sensor_values(state, temperature, humidity)
    
            except Exception as e:
                print('Error:', e)


             
