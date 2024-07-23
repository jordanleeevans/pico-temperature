import time
from machine import Pin
from config import MQTT_TOPIC

led = Pin("LED", Pin.OUT)

def light_onboard_led(status):
    if status == "on":
        led.on()
    elif status == "off":
        led.off()
    elif status == "blink":
        led.on()
        time.sleep(0.5)  # Adjust blink duration as needed
        led.off()

