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

def runner(temperature_sensor, mqtt_client):
    while True:
        temperature = temperature_sensor.read()
        if temperature > 80:
            # On boot the DS18X20 initialises its value to 85.0, so we ignore.
            continue
        mqtt_client.publish(MQTT_TOPIC, str(temperature))
        print(f"Publishing temperature {temperature} to {MQTT_TOPIC}")
        time.sleep(60)

