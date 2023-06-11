# boot.py -- run on boot-up

import secrets

def do_connect():
    from network import WLAN, STA_IF
    import time
    wlan = WLAN(STA_IF)  # get current object
    wlan.active(True)
    if not wlan.isconnected():          # Check if already connected
        print("Connecting to WiFi...")
        # Connect with your WiFi Credential
        wlan.connect(secrets.SSID, secrets.Password)
        # Check if it is connected otherwise wait
        while not wlan.isconnected():
            pass
    print("Connected to WiFi")
    time.sleep_ms(500)
    # Print the IP assigned by the router
    print('Network config:', wlan.ifconfig())

# WiFi Connection
do_connect()
