<b>Backend</b>

<b>Overview:</b>
This folder contains a simple Node.js backend server for the temperature project.  
It provides a RESTful API endpoint that returns simulated sensor data in JSON format.  
The backend can be used with the `temperature` folder project to fetch temperature and humidity readings.

<b>Files:</b>
- **server.js** &mdash; Node.js Express server providing `/api/sensor` endpoint.  
- **package.json** &mdash; Node.js project configuration.  
- **package-lock.json** &mdash; Lock file for dependencies.  
- **node_modules/** &mdash; Installed Node.js dependencies (do not modify manually).

<b>How it works:</b>
- Starts an Express server on port `3000`.  
- Provides a GET endpoint at `/api/sensor`.  
- Responds with JSON containing:
  - `temperature` – simulated temperature value (°C)  
  - `humidity` – simulated humidity value (%)  
  - `status` – status string (`"OK"`)

<b>Example JSON response:</b>

```json
{
  "temperature": 22.5,
  "humidity": 55,
  "status": "OK"
}
```
---

<b>temperature</b>

<b>Overview:</b>
This project demonstrates how to read temperature data from a DHT22 sensor using an ESP32 (or compatible board) and send it to ThingSpeak for remote monitoring.  
- Connects the ESP32 to Wi-Fi.  
- Reads temperature every 15 seconds.  
- Sends data to ThingSpeak via HTTP POST requests.  
- Prints readings and server responses to the serial console.

<b>Files:</b>
- **main.py** &mdash; Reads temperature sensor and posts data to ThingSpeak.  
- **diagram.json** &mdash; Wokwi wiring diagram showing DHT22 sensor connections.  
- **wokwi-project.txt** &mdash; Wokwi project link.

<b>Hardware:</b>
- ESP32
- DHT22 temperature sensor
- Jumper wires
- Breadboard (optional)

<b>Wiring:</b>
1. Connect DHT22 data pin to GPIO15 on ESP32.  
2. Connect DHT22 VCC to 3.3V and GND to ground.  
3. Use a pull-up resistor (typically 4.7k–10k Ω) between VCC and data pin if required.

<b>How to run (Wokwi):</b>
1. Open Wokwi and load the project using `wokwi-project.txt` or `diagram.json`.  
2. Run the simulation.  
3. Observe temperature readings printed in the console.  
4. Data will be sent to ThingSpeak (simulation may not perform real HTTP requests).

<b>Expected behavior:</b>
- Every 15 seconds, the ESP32 measures temperature.  
- Sends a POST request to ThingSpeak with `field1` containing the temperature.  
- Console prints temperature and ThingSpeak server response.
