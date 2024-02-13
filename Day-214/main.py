import datetime

class Houseplant:
    def __init__(self, name, species, acquisition_date, location):
        self.name = name
        self.species = species
        self.acquisition_date = acquisition_date
        self.location = location
        self.last_watered = None
        self.last_fertilized = None
        self.health_status = "Healthy"

    def water(self):
        self.last_watered = datetime.datetime.now()

    def fertilize(self):
        self.last_fertilized = datetime.datetime.now()

    def check_health(self):
        if self.last_watered is None:
            self.health_status = "Unknown (Not watered)"
        else:
            days_since_last_watered = (datetime.datetime.now() - self.last_watered).days
            if days_since_last_watered <= 2:
                self.health_status = "Healthy"
            elif days_since_last_watered <= 5:
                self.health_status = "Needs water soon"
            else:
                self.health_status = "Needs immediate watering"
class HouseplantCareAssistant:
    def __init__(self):
        self.plants = []

    def add_plant(self, plant):
        self.plants.append(plant)

    def water_plant(self, plant_name):
        for plant in self.plants:
            if plant.name == plant_name:
                plant.water()
                print(f"{plant_name} has been watered.")
                break
        else:
            print(f"No plant named {plant_name} found.")

    def fertilize_plant(self, plant_name):
        for plant in self.plants:
            if plant.name == plant_name:
                plant.fertilize()
                print(f"{plant_name} has been fertilized.")
                break
        else:
            print(f"No plant named {plant_name} found.")

    def display_plants(self):
        if not self.plants:
            print("No plants in the collection.")
        else:
            print("Plants in Collection:")
            for plant in self.plants:
                print(f"{plant.name} ({plant.species}) - Last watered: {plant.last_watered}, Last fertilized: {plant.last_fertilized}")

if __name__ == "__main__":
    assistant = HouseplantCareAssistant()

    plant1 = Houseplant("Peace Lily", "Spathiphyllum", datetime.date(2023, 1, 1), "Living Room")
    plant2 = Houseplant("Snake Plant", "Sansevieria trifasciata", datetime.date(2023, 1, 15), "Bedroom")
    assistant.add_plant(plant1)
    assistant.add_plant(plant2)

    assistant.water_plant("Peace Lily")
    assistant.fertilize_plant("Snake Plant")

    assistant.display_plants()
