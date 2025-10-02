## IoT_perusteet

This repository contains all exercises and projects from my IoT software course in LAB University of Applied Sciences in Sept/Oct 2025. Each lesson focuses on different aspects of IoT, including MicroPython programming, sensors, real-time communication, dashboards, and backend integration.

---

### **<a href="https://github.com/smyllykoski/IoT_perusteet/tree/main/Lesson_1">Lesson 1:</a> MicroPython Basics and Sensors** 

**Folders:**  
- `blink_external_led` &mdash; Blink an external LED.  
- `blink_onboard_led` &mdash; Blink the onboard LED with example tasks.  
- `burglar_alarm` &mdash; PIR motion sensor triggers a buzzer/LED alarm.  
- `interrupt` &mdash; Reaction time measurement using button interrupts.  
- `traffic_lights` &mdash; Simulates a traffic light sequence with button override.  
- `turn_led_on_with_button` &mdash; Turn LED on/off using a button.  
- `weather_station` &mdash; Reads DHT22 temperature and humidity.  
- `weather_station_with_backend` &mdash; Reads sensor data and sends it to ThingSpeak.  

---

### **<a href="https://github.com/smyllykoski/IoT_perusteet/tree/main/Lesson_2">Lesson 2:</a> Backend Integration**

**Folders:**  
- `Backend` – Node.js server with REST API endpoints.  
- `temperature` – MicroPython project sending sensor data to ThingSpeak.  

---

### **<a href="https://github.com/smyllykoski/IoT_perusteet/tree/main/Lesson_3">Lesson 3:</a> Databases and Persistent Storage**

**Files:**  
- `server.js` – Node.js server using SQLite to store and retrieve user data.  

---

### **<a href="https://github.com/smyllykoski/IoT_perusteet/tree/main/Lesson_4">Lesson 4:</a> Real-Time Communication and Dashboards**

**Folders:**  
- `Fetch` – Fetch sensor data from ThingSpeak using JavaScript.  
- `GoogleChart` – Display ThingSpeak data as a Google Chart.  
- `Webhook` – Node.js server receiving POST requests to trigger actions (e.g., Discord notifications).  
- `Websocket` – WebSocket client and server example for real-time sensor updates.  

---

### **Usage Notes**

- **MicroPython code** runs on Wokwi simulator or compatible IoT hardware (e.g., Raspberry Pi Pico W).  
- **Node.js code** requires Node.js installed locally; run `npm install` in each backend folder.  
- **Web dashboards** can be opened in a browser and updated with live IoT data using webhooks or WebSockets.  
