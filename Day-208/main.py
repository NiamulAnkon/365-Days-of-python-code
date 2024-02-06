import time
import random

class Smart_HomeEnergy_Management_System:
    def __init__(self):
        self.energy_usage = 0
        self.appliances = {'Fridge': 100, 'AC': 200, 'Lights': 50, 'TV': 150}
        self.energy_costs = {'Off-Peak': 0.10, 'Peak': 0.15}
    
    def main_menu(self):
        while True:
            print("\n--- Smart Home Energy Management System ---")
            print("1. View Energy Usage")
            print("2. Turn On/Off Appliances")
            print("3. Check Energy Costs")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.view_energy_usage()
            elif choice == '2':
                self.control_appliances()
            elif choice == '3':
                self.check_energy_costs()
            elif choice == '4':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Try again.")
    
    def view_energy_usage(self):
        print(f"\nCurrent Energy Usage: {self.energy_usage} kWh")
    
    def control_appliances(self):
        print("\n--- Control Appliances ---")
        for idx, appliance in enumerate(self.appliances.keys(), start=1):
            print(f"{idx}. {appliance}")
        appliance_choice = int(input("Enter the number of the appliance to turn On/Off: "))
        if 1 <= appliance_choice <= len(self.appliances):
            appliance_name = list(self.appliances.keys())[appliance_choice - 1]
            if appliance_name in self.appliances:
                self.toggle_appliance(appliance_name)
        else:
            print("Invalid appliance choice.")
    
    def toggle_appliance(self, appliance_name):
        energy_consumption = self.appliances[appliance_name]
        if appliance_name in self.appliances:
            print(f"{appliance_name} is turned {'Off' if energy_consumption == 0 else 'On'}")
            self.energy_usage += energy_consumption if energy_consumption > 0 else -energy_consumption
    
    def check_energy_costs(self):
        print("\n--- Energy Costs ---")
        for period, cost in self.energy_costs.items():
            print(f"{period}: ${cost:.2f} per kWh")

if __name__ == "__main__":
    shems = Smart_HomeEnergy_Management_System()
    shems.main_menu()
