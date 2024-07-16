import time
from wifi import WifiConnection
from sensor import TemperatureSensor
from config import SSID, PASSWORD, MQTT_CLIENT_ID, MQTT_SERVER, MQTT_PORT, MQTT_USER, MQTT_PASSWORD, MQTT_TOPIC
from umqtt.simple import MQTTClient
from utils import light_onboard_led

temperature_sensor = TemperatureSensor(
    id="01",
    name="Temperature Sensor",
    description="DS18X20 temperature sensor",
    location="Utility Room",
    unit="Celsius",
    pin=16
)

with WifiConnection(ssid=SSID, password=PASSWORD) as wifi:
    
    if wifi.wlan.status() >=3:
        light_onboard_led("on")
        
    mqtt_client = MQTTClient(
        client_id=MQTT_CLIENT_ID,
        server=MQTT_SERVER,
        port=MQTT_PORT,
        user=MQTT_USER,
        password=MQTT_PASSWORD
    )
    
    mqtt_client.connect()
    
    while True:
        temperature = temperature_sensor.read()
        if temperature > 80:
            # On boot the DS18X20 initialises its value to 85.0, so we ignore.
            continue
        mqtt_client.publish(MQTT_TOPIC, str(temperature))
        print(f"Published temperature of {temperature}°C to {MQTT_TOPIC}")
        time.sleep(60)
