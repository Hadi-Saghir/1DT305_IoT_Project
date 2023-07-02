import network
import time
from secrets import secrets

class ConnectionHandler:
    def __init__(self):
        self.ssid = secrets['WIFI_SSID']
        self.password = secrets['WIFI_PASSWORD']
        self.wifi = network.WLAN(network.STA_IF)
        self.wifi.active(True)

    def connect_to_wifi(self):
        self.wifi.connect(self.ssid, self.password)
        max_tries = 3
        for _ in range(max_tries):
            if self.wifi.isconnected():
                break
            time.sleep(3)
            print("Failed to connect to WiFi")
            self.wifi.connect(self.ssid, self.password)
        else:
            raise Exception("Failed to connect to WiFi after multiple tries.")
        
        print("Connected to WiFi:", self.ssid)
        print("IP address:", self.wifi.ifconfig()[0])

    def check_wifi_connection(self):
        if not self.wifi.isconnected():
            print("WiFi connection lost. Reconnecting...")
            self.connect_to_wifi()
            return True
    

