import machine
import network
import time
import dht
import urequests
from machine import Pin

# Wi-fi configuration
ssid = 'Wokwi-GUEST'    # SSID of the Wi-Fi network
password = ''           # Password (empty for open networks like Wokwi-GUEST)

# ThingSpeak API configuration
THINGSPEAK_API_KEY = 'HMMXI2BNF7LZONDG'  # Your ThingSpeak Write API Key
THINGSPEAK_URL = 'https://api.thingspeak.com/update'  # ThingSpeak endpoint

# Set up Wi-Fi in station mode

wlan = network.WLAN(network.STA_IF)  # Create a WLAN object in station mode, the device connects to a Wi-Fi network as a client. 
wlan.active(True)                    # Activate the Wi-Fi interface
wlan.connect(ssid, password)         # Connect to the specified Wi-Fi network

# Wait until connected
print("Connecting to Wi-Fi...", end="")
while not wlan.isconnected():
    print(".", end="")               # Print dots while waiting
    time.sleep(0.5)                  # Wait half a second before retrying

# Once connected, print confirmation and IP address
print("\nConnected!")
print("IP address:", wlan.ifconfig()[0])  # Display the assigned IP address

# initialize DHT22 sensor on GPIO15
sensor = dht.DHT22(machine.Pin(15))

# Function to send temperature data to ThingSpeak
def send_to_thingspeak(temp, hum):
    try:
        data='api_key={}&field1={}&field2={}'.format(THINGSPEAK_API_KEY, temp, hum)
        # Send HTTP POST request to ThingSpeak with temperature data
        response = urequests.post(
            THINGSPEAK_URL,
            data = data,            
            headers={'Content-Type': 'application/x-www-form-urlencoded'}
        )
        print("ThingSpeak response:", response.text)  # Print server response
        response.close()  # Close the connection
    except Exception as e:
        print("Failed to send data:", e)  # Handle any errors

while True:
    try:
        sensor.measure()
        temperature = sensor.temperature()
        humidity = sensor.humidity()

        print("Temperature: {:.1f} C".format(temperature))
        print("Humidity: {:.1f}%".format(humidity))

        send_to_thingspeak(temperature, humidity)

    except OSError as e:
        print("Sensor read error: ", e)

    time.sleep(15)