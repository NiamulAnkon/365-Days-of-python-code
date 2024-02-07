class Smart_Home_Automation_System:
    def __init__(self):
        self.devices = {}  
        self.user_profiles = {}  
        
    def add_device(self, device_name, device_type):
        self.devices[device_name] = {'type': device_type, 'state': 'off'}
        
    def remove_device(self, device_name):
        if device_name in self.devices:
            del self.devices[device_name]
        else:
            print("Device not found.")
        
    def control_device(self, device_name, action):
        if device_name in self.devices:
            if action == 'on':
                self.devices[device_name]['state'] = 'on'
            elif action == 'off':
                self.devices[device_name]['state'] = 'off'
            else:
                print("Invalid action.")
        else:
            print("Device not found.")
        
    def create_user_profile(self, username):
        self.user_profiles[username] = {}
        
    def add_device_to_profile(self, username, device_name):
        if username in self.user_profiles and device_name in self.devices:
            self.user_profiles[username][device_name] = self.devices[device_name]
        else:
            print("User or device not found.")
        
    def remove_device_from_profile(self, username, device_name):
        if username in self.user_profiles and device_name in self.user_profiles[username]:
            del self.user_profiles[username][device_name]
        else:
            print("User or device not found.")
        
    def display_user_profile(self, username):
        if username in self.user_profiles:
            print(f"User Profile: {username}")
            for device_name, device_info in self.user_profiles[username].items():
                print(f"{device_name}: {device_info['type']} - {device_info['state']}")
        else:
            print("User not found.")
            
    def display_all_devices(self):
        print("Devices in the System:")
        for device_name, device_info in self.devices.items():
            print(f"{device_name}: {device_info['type']} - {device_info['state']}")

if __name__ == "__main__":
    smart_home = Smart_Home_Automation_System()
    
    smart_home.add_device('Living Room Light', 'light')
    smart_home.add_device('Bedroom Light', 'light')
    smart_home.add_device('Smart Thermostat', 'thermostat')
    
    smart_home.control_device('Living Room Light', 'on')
    
    smart_home.create_user_profile('John')
    smart_home.create_user_profile('Alice')
    
    smart_home.add_device_to_profile('John', 'Living Room Light')
    smart_home.add_device_to_profile('John', 'Smart Thermostat')
    smart_home.add_device_to_profile('Alice', 'Bedroom Light')
    
    smart_home.display_user_profile('John')
    smart_home.display_user_profile('Alice')
    smart_home.display_all_devices()
