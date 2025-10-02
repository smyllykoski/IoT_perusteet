<b>blink_external_led</b>

<p><b>Overview:</b> This simple project demonstrates how to blink an external LED using an ESP32 (MicroPython). The LED toggles on/off at a fixed interval.</p>

<p><b>Files:</b></p>
<ul>
  <li><b>main.py</b> &mdash; MicroPython script that blinks the external LED.</li>
  <li><b>diagram.json</b> &mdash; Wokwi wiring diagram for the project.</li>
  <li><b>wokwi-project.txt</b> &mdash; Wokwi project link (open this in Wokwi to run simulation).</li>
</ul>

<p><b>Hardware:</b></p>
<ul>
  <li>ESP32 development board (or equivalent)</li>
  <li>1 × LED (any color)</li>
  <li>1 × 220&ndash;330 Ω resistor</li>
  <li>Jumper wires and breadboard (if using physical hardware)</li>
</ul>

<p><b>Typical wiring:</b></p>
<ol>
  <li>Connect the LED anode (long leg) to an ESP32 GPIO pin (e.g. <b>GPIO15</b>) via a 220 Ω resistor.</li>
  <li>Connect the LED cathode (short leg) to <b>GND</b>.</li>
  <li>Check <code>diagram.json</code> for the exact wiring used in the Wokwi simulation.</li>
</ol>

<p><b>How to run (Wokwi):</b></p>
<ol>
  <li>Open Wokwi and load the project using <code>wokwi-project.txt</code> or by importing <code>diagram.json</code>.</li>
  <li>Run the simulation. The LED should blink at the interval defined in <code>main.py</code>.</li>
</ol>

<p><b>Expected behavior:</b></p>
<ul>
  <li>The external LED toggles ON for a short period and OFF for a short period in a loop.</li>
  <li>Typical blink interval in <code>main.py</code> is 0.5 &ndash; 1.0 seconds (adjustable in code).</li>
</ul>

---

<b>blink_on_board_led</b>

<b>Overview:</b>
This project demonstrates basic LED control, loops, and conditional input on the ESP32 with MicroPython.  
The main script blinks the onboard LED, and the additional exercises (`tehtava1.py`, `tehtava2.py`) illustrate loops and conditional statements.

<b>Files:</b>
- **main.py** &mdash; Blinks the onboard LED with a 1-second interval.
- **tehtava1.py** &mdash; Demonstrates a simple `for` loop that counts from 0 to 9 and prints each iteration.
- **tehtava2.py** &mdash; Demonstrates user input and conditionals. It asks for a name and prints a message based on the input.
- **diagram.json** &mdash; Wokwi wiring diagram (uses the built-in LED).
- **wokwi-project.txt** &mdash; Wokwi project link.

<b>Hardware required:</b>
- ESP32 (or any board with an onboard LED pin).

<b>How to run (Wokwi):</b>
1. Open Wokwi and load the project using `wokwi-project.txt` or `diagram.json`.
2. Run the simulation. The onboard LED will blink once per second (main.py).
3. To test `tehtava1.py` or `tehtava2.py`, replace the code in the ESP32 with the respective script and observe the serial output.

<b>Expected behavior</b>
- **main.py**: The onboard LED turns ON for 1 second and OFF for 1 second continuously.
- **tehtava1.py**: Serial console prints numbers from 0 to 9, then ends the loop.
- **tehtava2.py**: Serial console prompts "What is your name:".  
  - If the user types `Clark Kent`, it prints `You are Superman!`.  
  - Otherwise, it prints `You are a regular human being.`

---

<b>burglar_alarm</b>

<b>Overview:</b>
This project demonstrates how to use a PIR motion sensor with an ESP32 to detect motion and trigger an alarm.  
When motion is detected, a message is printed to the serial console, and the onboard LED flashes as a visual alarm.

<b>Files:</b>
- **main.py** &mdash; Reads the PIR sensor and flashes the onboard LED when motion is detected.
- **diagram.json** &mdash; Wokwi wiring diagram showing the PIR sensor and ESP32 connections.
- **wokwi-project.txt** &mdash; Wokwi project link.

<b>Hardware required:</b>
- ESP32 (or compatible board with onboard LED)
- PIR motion sensor
- Jumper wires

<b>Wiring:</b>
1. Connect PIR sensor output to GPIO28 on the ESP32.
2. Connect PIR sensor power (VCC) and ground (GND) appropriately.
3. Onboard LED is used for visual feedback (no extra components needed).

<b>How to run (Wokwi):</b>
1. Open Wokwi and load the project using `wokwi-project.txt` or `diagram.json`.
2. Run the simulation.  
3. Trigger motion in the simulation (if supported) and observe the LED flashing and the console message.

<b>Expected behavior:</b>
- LED toggles rapidly for 50 iterations (~5 seconds total) whenever the PIR sensor detects motion.
- Console prints `"ALARM! Motion detected!"`.

---

<b>interrupt</b>

<b>Overview:</b>
This project demonstrates how to use an **interrupt** on an ESP32/Pico W to measure reaction time.  
The onboard LED turns on for a random interval (5–10 seconds), then turns off, signaling the user to press a button. The time between the LED turning off and the button press is measured and printed in milliseconds.

<b>Files:</b>
- **main.py** &mdash; Uses an LED, button, and interrupt to measure reaction time.
- **diagram.json** &mdash; Wokwi wiring diagram showing LED and button connections.
- **wokwi-project.txt** &mdash; Wokwi project link.

<b>Hardware:</b>
- ESP32 or Raspberry Pi Pico W
- LED
- Push button
- Resistor for the button pull-down (if not using internal pull-down)
- Jumper wires

<b>Wiring:</b>
1. Connect the LED anode to GPIO15 via a resistor; cathode to GND.
2. Connect one side of the button to GPIO14 and the other side to GND (internal pull-down enabled in code).

<b>How to run (Wokwi):</b>
1. Open Wokwi and load the project using `wokwi-project.txt` or `diagram.json`.
2. Run the simulation.
3. Observe the LED: it will turn on for a random time, then off. Press the button after it goes off.
4. The console prints your reaction time in milliseconds.

<b>Expected behavior:</b>
- LED turns on for 5–10 seconds, then turns off.
- User presses button after LED goes off.
- Serial console prints: `"Your reaction time was X milliseconds"` followed by `"Program complete."`

---

<b>traffic_lights</b>

<b>Overview:</b>
This project simulates a traffic light system using an ESP32 with three LEDs (red, yellow, green), a push button, and a buzzer.  
- The traffic light sequence runs automatically in a loop.  
- When the button is pressed, the red light turns on and the buzzer sounds for a short period.  

<b>Files:</b>
- **main.py** &mdash; Controls the traffic light sequence, button detection, and buzzer beep.
- **diagram.json** &mdash; Wokwi wiring diagram showing LEDs, button, and buzzer connections.
- **wokwi-project.txt** &mdash; Wokwi project link.

<b>Hardware:</b>
- ESP32
- 3 LEDs (red, yellow, green)
- 3 resistors (220–330 Ω)
- Push button
- Buzzer
- Jumper wires

<b>Wiring:</b>
1. Connect each LED anode to GPIO pins:  
   - Red to GPIO15  
   - Yellow to GPIO14  
   - Green to GPIO13  
   Each LED goes through a resistor to GND.  
2. Connect button to GPIO16 with internal pull-down enabled.  
3. Connect buzzer to GPIO12 with GND.

<b>How to run (Wokwi):</b>
1. Open Wokwi and load the project using `wokwi-project.txt` or `diagram.json`.
2. Run the simulation.  
3. Observe the traffic light sequence: red → red+yellow → green → yellow.  
4. Press the button to trigger the buzzer and red light.

<b>Expected behavior:</b>
- LEDs cycle through the traffic light pattern with the configured timings:  
  - Red: 2 s  
  - Red + Yellow: 2 s  
  - Green: 5 s  
  - Yellow: 2 s  
- Pressing the button:  
  - Red LED turns on  
  - Buzzer sounds for ~2 seconds  
  - Sequence continues normally after.

---

<b>turn_led_on_with_button</b>

<b>Overview:</b>
This project demonstrates how to control an LED using a push button with an ESP32.  
- When the button is pressed, the LED turns on.  
- When the button is released, the LED turns off.

<b>Files:</b>
- **main.py** &mdash; Reads button state and controls the LED accordingly.
- **diagram.json** &mdash; Wokwi wiring diagram showing LED and button connections.
- **wokwi-project.txt** &mdash; Wokwi project link.

<b>Hardware:</b>
- ESP32
- LED
- 220–330 Ω resistor for LED
- Push button
- Jumper wires

<b>Wiring:</b>
1. Connect LED anode to GPIO18 via a resistor; cathode to GND.  
2. Connect button to GPIO13; internal pull-up is enabled in code.

<b>How to run (Wokwi):</b>
1. Open Wokwi and load the project using `wokwi-project.txt` or `diagram.json`.  
2. Run the simulation.  
3. Press the button: LED should turn on while pressed and off when released.

<b>Expected behavior:</b>
- LED turns ON when button is pressed (button value = 0 due to pull-up).  
- LED turns OFF when button is released.

---

<b>weather_station</b>

<b>Overview:</b>
This project uses a DHT22 sensor to measure temperature and humidity. The values are read every 2 seconds and printed to the serial console.

<b>Files:</b>
<ul>
  <li><b>main.py</b> &mdash; Reads DHT22 data (temperature & humidity).</li>
  <li><b>diagram.json</b> &mdash; Wiring diagram for ESP32 + DHT22.</li>
  <li><b>wokwi-project.txt</b> &mdash; Wokwi project link.</li></ul>

<b>Hardware:</b>
<ul>
  <li>ESP32</li>
  <li>DHT22 sensor (data pin connected to GPIO15)</li></ul>

<b>How to run:</b>
<ol>
<li>Connect the DHT22 sensor to ESP32 as in diagram.json.</li>
<li>Upload code to ESP32 or run in Wokwi.</li>
<li>Open the serial console to see temperature and humidity readings.</li>
</ol>

---

<b>weather_station_with_backend</b>

<b>Overview:</b>
This project extends the basic weather station by connecting the ESP32 to Wi-Fi and sending sensor data to ThingSpeak.  
- Reads temperature and humidity from a DHT22 sensor.  
- Sends data to ThingSpeak every 15 seconds.  
- Prints sensor readings and ThingSpeak responses to the serial console.

<b>Files:</b>
- **main.py** &mdash; Reads DHT22 sensor and posts data to ThingSpeak.  
- **diagram.json** &mdash; Wokwi wiring diagram showing DHT22 sensor connections.  
- **wokwi-project.txt** &mdash; Wokwi project link.

<b>Hardware:</b>
- ESP32
- DHT22 sensor
- Jumper wires
- Breadboard (optional)

<b>Wiring:</b>
1. Connect DHT22 data pin to GPIO15 on ESP32.  
2. Connect DHT22 VCC to 3.3V and GND to ground.  
3. Use a pull-up resistor (typically 4.7k–10k Ω) between VCC and data pin if required.

<b>How to run (Wokwi):</b>
1. Open Wokwi and load the project using `wokwi-project.txt` or `diagram.json`.  
2. Run the simulation.  
3. Observe temperature and humidity printed in the console.  
4. Check ThingSpeak channel to see the data updates (simulation may not send real HTTP requests).

<b>Expected behavior:</b>
- Every 15 seconds, the ESP32 measures temperature and humidity.  
- Sends a POST request to ThingSpeak with `field1` = temperature, `field2` = humidity.  
- Console prints readings and ThingSpeak server response.
