import requests

# Your local endpoint
url = "http://gena:3000"

# Send a GET request to the local endpoint
response = requests.get(url)

if response.status_code == 200:
    print("Endpoint is working fine!")
    print(response.text)
else:
    print(f"Error with the local endpoint: {response.status_code}")
    print(response.text)
