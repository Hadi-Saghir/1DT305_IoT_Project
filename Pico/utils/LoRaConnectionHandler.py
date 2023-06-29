import socket
import struct
from network import LoRa
import time
import _thread

class ConnectionHandler:
    def __init__(self):
        self.lora = None
        self.lora_sock = None
        self.last_msg_id = -1
        self._LORA_PKG_FORMAT = "!BBffffff"
        self._LORA_PKG_ACK_FORMAT = "BBB"
    
    def connect(self):
        self.start_lora()
        time.sleep(1)
        
        _thread.start_new_thread(self.listen_to_lora, ())
    
    def start_lora(self):
        self.lora = LoRa(mode=LoRa.LORA, rx_iq=True, region=LoRa.EU868)
        self.lora_sock = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
        self.lora_sock.setblocking(False)
        print('LoRa connection established')
    
    def listen_to_lora(self):
        while True:
            recv_pkg = self.lora_sock.recv(512)
            if len(recv_pkg) == 26:
                print("Package received")
                print(recv_pkg)

                try:
                    device_id, msg_id, indoorTemp, outdoorTemp, indoorHumid, outdoorHumid, eco2, etvoc = struct.unpack(self._LORA_PKG_FORMAT, recv_pkg)
                except:
                    continue

                if device_id == 0x01 and self.last_msg_id == msg_id:
                    continue
                self.last_msg_id = msg_id

                payload = {
                    "temperature": indoorTemp,
                    "humidity": indoorHumid
                }

                ack_pkg = struct.pack(self._LORA_PKG_ACK_FORMAT, device_id, msg_id, 200)
                self.lora_sock.send(ack_pkg)
                print("sent ack")

                _thread.start_new_thread(self.pub_sensor_values, [payload])

            time.sleep(0.2)
        
    def pub_sensor_values(self, topic, temperature, humidity):
        # Create the message dictionary
        message = {
            "temperature": "{{temperature}}",
            "humidity": "{{humidity}}"
        }

        # Fill in the dynamic values in the message template
        message["temperature"] = temperature
        message["humidity"] = humidity

        # Convert the message to JSON
        json_message = json.dumps(message)

        # Send the JSON message using your desired method
        # For example, you can publish it to an MQTT topic
        client.publish(topic=topic, msg=json_message)
        
    def listen_to_lora(self):
        # LoRa receive logic
        
    def run(self):
        # Initialize LoRa and other components
        # Connect to MQTT server
        # Start listening to LoRa
