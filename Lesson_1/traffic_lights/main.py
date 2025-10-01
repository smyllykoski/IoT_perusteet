import machine
import utime

led_red = machine.Pin(15, machine.Pin.OUT)
led_yellow = machine.Pin(14, machine.Pin.OUT)
led_green = machine.Pin(13, machine.Pin.OUT)
button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
buzzer = machine.Pin(12, machine.Pin.OUT)

RED_TIME = 2
RED_YELLOW_TIME = 2
GREEN_TIME = 5
YELLOW_TIME = 2

def beep_buzzer(duration=2):
    start = utime.ticks_ms()
    while utime.ticks_diff(utime.ticks_ms(), start) < duration*1000:
        buzzer.value(1)
        utime.sleep(0.2)
        buzzer.value(0)
        utime.sleep(0.2)

while True:
    if button.value() == 1:
        led_red.value(1)
        beep_buzzer(duration=2)
        led_red.value(0)

    # Traffic light sequence
    led_red.value(1)
    utime.sleep(RED_TIME)
    led_yellow.value(1)
    utime.sleep(RED_YELLOW_TIME)
    led_red.value(0)
    led_yellow.value(0)
    led_green.value(1)
    utime.sleep(GREEN_TIME)
    led_green.value(0)
    led_yellow.value(1)
    utime.sleep(YELLOW_TIME)
    led_yellow.value(0)