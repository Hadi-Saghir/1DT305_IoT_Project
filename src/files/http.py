import urequests

node_red_url = "http://192.168.1.111:1880"
endpoint = "/brewing/check-sound"

# HTTP GET request
response = urequests.get(node_red_url + endpoint)

# Print the response
print(response.text)

# Close the response
response.close()
