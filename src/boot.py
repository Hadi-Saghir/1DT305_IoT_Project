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
        wlan.connect(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)
        # Check if it is connected otherwise wait
        while not wlan.isconnected():
            pass
    print("Connected to WiFi")
    time.sleep_ms(500)
    # Print the IP assigned by the router
    ip_address = wlan.ifconfig()[0]
    print("IP address:", ip_address)

# WiFi Connection
do_connect()
