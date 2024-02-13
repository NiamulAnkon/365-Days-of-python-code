import time
import random

class GreenhouseAutomationSystem:
    def __init__(self):
        self.temperature = 0
        self.humidity = 0
        self.soil_moisture = 0
        self.light_intensity = 0

    def read_sensor_data(self):
        self.temperature = random.randint(20, 30)
        self.humidity = random.randint(40, 70)
        self.soil_moisture = random.randint(0, 100)
        self.light_intensity = random.randint(500, 1000)

    def control_environment(self):
        if self.temperature > 25:
            print("Temperature too high. Turning on cooling system.")
        elif self.temperature < 20:
            print("Temperature too low. Turning on heating system.")
        
        if self.soil_moisture < 50:
            print("Soil moisture too low. Initiating irrigation.")
        elif self.soil_moisture > 80:
            print("Soil moisture too high. Stopping irrigation.")
        
        if self.light_intensity < 700:
            print("Low light intensity. Turning on supplemental lighting.")
        elif self.light_intensity > 900:
            print("High light intensity. Turning off supplemental lighting.")

    def start(self):
        while True:
            self.read_sensor_data()
            self.control_environment()
            time.sleep(5)

if __name__ == "__main__":
    system = GreenhouseAutomationSystem()
    system.start()
