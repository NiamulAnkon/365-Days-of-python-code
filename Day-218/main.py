import json
import os
import datetime

class DigitalTimeCapsule:
    def __init__(self):
        self.time_capsules = []

    def create_time_capsule(self, name, description, opening_date):
        self.time_capsules.append({
            "name": name,
            "description": description,
            "opening_date": opening_date,
            "memories": []
        })

    def add_memory(self, time_capsule_index, memory):
        self.time_capsules[time_capsule_index]["memories"].append(memory)

    def view_time_capsules(self):
        for idx, capsule in enumerate(self.time_capsules):
            print(f"{idx + 1}. {capsule['name']} (Opening Date: {capsule['opening_date']})")

    def view_memories(self, time_capsule_index):
        for idx, memory in enumerate(self.time_capsules[time_capsule_index]["memories"]):
            print(f"{idx + 1}. {memory}")

    def save_to_file(self):
        with open("time_capsules.json", "w") as file:
            json.dump(self.time_capsules, file)

    def load_from_file(self):
        if os.path.exists("time_capsules.json"):
            with open("time_capsules.json", "r") as file:
                self.time_capsules = json.load(file)


def main():
    dtc = DigitalTimeCapsule()
    dtc.load_from_file()

    while True:
        print("\n1. Create Time Capsule")
        print("2. Add Memory")
        print("3. View Time Capsules")
        print("4. View Memories")
        print("5. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the name of the time capsule: ")
            description = input("Enter a description for the time capsule: ")
            opening_date = input("Enter the opening date (YYYY-MM-DD): ")
            dtc.create_time_capsule(name, description, opening_date)
            print("Time capsule created successfully!")

        elif choice == "2":
            dtc.view_time_capsules()
            time_capsule_index = int(input("Enter the index of the time capsule: ")) - 1
            memory = input("Enter the memory to add: ")
            dtc.add_memory(time_capsule_index, memory)
            print("Memory added successfully!")

        elif choice == "3":
            dtc.view_time_capsules()

        elif choice == "4":
            dtc.view_time_capsules()
            time_capsule_index = int(input("Enter the index of the time capsule: ")) - 1
            dtc.view_memories(time_capsule_index)

        elif choice == "5":
            dtc.save_to_file()
            print("Data saved successfully. Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
