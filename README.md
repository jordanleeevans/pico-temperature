# Raspberry Pi Pico WH MQTT Publisher

This project is a simple example of how to use the [Raspberry Pi Pico WH](https://thepihut.com/products/raspberry-pi-pico-w?variant=41952994787523) to publish data to an MQTT broker. This is used in my homelab to monitor the temperature and humidity in my server room. The data is published to an MQTT broker hosted on my server and displayed in my home assistant dashboard.

On boot the Pico will run `main.py` which will read the temperature from the [DS18X20](https://thepihut.com/products/waterproof-ds18b20-digital-temperature-sensor-extras?variant=27740417873&currency=GBP&utm_medium=product_sync&utm_source=google&utm_content=sag_organic&utm_campaign=sag_organic&gad_source=1&gclid=CjwKCAjwtNi0BhA1EiwAWZaANBnhGe2AJmlLG1U24ey2xiXdPbHhvD46_rXT4ldNFK6NyepNgkVHZhoCweYQAvD_BwE) sensor and publish it to the MQTT broker every 60 seconds. The onboard LED initially activates once a WiFi connection has been established and then blinks every time data is published.

## Configuration

 The config file is not included in this repository. You will need to create a `config.py` file in the root directory with your WiFi and MQTT broker details.

## Hardware

- Raspberry Pi Pico WH
- DS18X20 Temperature Sensor
- 4.7k Resistor
- Breadboard
- 3x Jumper Wires
- USB Cable

## Connection Diagram

<p align="center">
  <img src="https://how2electronics.com/wp-content/uploads/2022/01/DS18B20-Raspberry-Pi-Pico-1.jpg" alt="Connection Diagram of Pi Pico WH">
</p>