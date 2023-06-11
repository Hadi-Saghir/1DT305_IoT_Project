def http_get(url='http://detectportal.firefox.com/'):
    import socket                           # Used by HTML get request
    import time                             # Used for delay
    _, _, host, path = url.split('/', 3)    # Separate URL request
    addr = socket.getaddrinfo(host, 80)[0][-1]  # Get IP address of host
    s = socket.socket()                     # Initialize the socket
    s.connect(addr)                         # Try connecting to the host address
    # Send HTTP request to the host with the specific path
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    time.sleep(1)                           # Sleep for a second
    rec_bytes = s.recv(10000)               # Receive response
    print(rec_bytes)                        # Print the response
    s.close()                               # Close the connection


# Connect to WiFi and perform HTTP request
http_get()






# wlan.connect('It burns when IP', auth=(WLAN.WPA2, 'Marionaoum1'))