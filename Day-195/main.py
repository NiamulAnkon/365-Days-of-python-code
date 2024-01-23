import random

class LanguageLearningRPG:
    def __init__(self):
        self.user_character = {
            'name': input("Enter your character's name: "),
            'language_proficiency': 1,
            'experience': 0,
        }

    def explore_game_world(self):
        print("Welcome to the Language Learning RPG!")
        print("You find yourself in a vast game world with different regions.")

        while True:
            print("\nOptions:")
            print("1. Explore a new region")
            print("2. Check character status")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.explore_region()
            elif choice == '2':
                self.display_character_status()
            elif choice == '3':
                print("Exiting the game. Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

    def explore_region(self):
        print("\nExploring a new region...")
        language_difficulty = random.randint(1, 5)  # Simulating difficulty levels
        print(f"This region has a language difficulty of {language_difficulty}.")

        # Simulate language learning challenges
        learning_success = random.choice([True, False])
        if learning_success:
            print("Congratulations! You successfully learned from this region.")
            self.user_character['experience'] += 10
            self.user_character['language_proficiency'] += 1
        else:
            print("Learning from this region was challenging. Keep practicing!")

    def display_character_status(self):
        print("\nCharacter Status:")
        print(f"Name: {self.user_character['name']}")
        print(f"Language Proficiency: {self.user_character['language_proficiency']}")
        print(f"Experience Points: {self.user_character['experience']}")

if __name__ == "__main__":
    game = LanguageLearningRPG()
    game.explore_game_world()
