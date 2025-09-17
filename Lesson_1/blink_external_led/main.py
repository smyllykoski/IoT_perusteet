import machine
import time
time.sleep(0.1)

led = machine.Pin(15, machine.Pin.OUT)

while True:
  led.value(1)
  time.sleep(1)
  led.value(0)
  time.sleep(1)