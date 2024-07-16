from machine import Pin
import onewire, ds18x20

class Sensor:
    """Sensor base class for Raspberry Pi Pico WH"""
    def __init__(self, id, name, description, location, unit, pin):
        self.id = id
        self.name = name
        self.description = description
        self.location = location
        self.unit = unit
        self.pin = Pin(pin, Pin.IN)

    def __str__(self):
        return f"Sensor(name={self.name}, pin={self.pin})"

    def __repr__(self):
        return self.__str__()

    def read(self):
        raise NotImplementedError
    
class TemperatureSensor(Sensor):
    def __init__(self, id, name, description, location, unit, pin):
        super().__init__(id, name, description, location, unit, pin)
        
    def read(self):
        sensor = ds18x20.DS18X20(onewire.OneWire(self.pin))
        roms = sensor.scan()
        
        if not roms:
            raise Exception("No DS18X20 devices found")
        
        if len(roms) > 1:
            raise Exception("Multiple DS18X20 devices found, please use a single sensor device.")
        
        sensor.convert_temp()

        return sensor.read_temp(roms[0])
