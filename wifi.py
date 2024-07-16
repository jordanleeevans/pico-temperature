import network, time
from config import SSID, PASSWORD

class WifiConnection:
    def __init__(self, ssid, password):
        self.ssid = ssid
        self.password = password
        
    def __enter__(self):
        if self.connect():
            return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()
        
    def connect(self):
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)
        if not self.wlan.isconnected():
            print(f'Connecting to WiFi: {SSID}')
            self.wlan.connect(SSID, PASSWORD)
            while not self.wlan.isconnected():
                time.sleep(1)
                print(".", end="")
            self.ip = self.wlan.ifconfig()[0]
        return True
    
    def disconnect(self):
        self.wlan.disconnect()
