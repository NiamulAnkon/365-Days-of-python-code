import json

class EcoPalLivingApp:
    def __init__(self):
        self.challenges = self.load_challenges()
        self.completed_challenges = set()

    def load_challenges(self):
        try:
            with open('challenges.json', 'r') as file:
                challenges = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            challenges = []
        return challenges

    def save_challenges(self):
        with open('challenges.json', 'w') as file:
            json.dump(self.challenges, file, indent=2)

    def display_challenges(self):
        print("EcoPal - Sustainable Living\n")
        print("Available Challenges:")
        for challenge in self.challenges:
            status = "Completed" if challenge['id'] in self.completed_challenges else "Not Completed"
            print(f"{challenge['id']}. {challenge['title']} - {challenge['description']} [{status}]")

    def add_challenge(self, title, description):
        new_challenge = {
            'id': len(self.challenges) + 1,
            'title': title,
            'description': description
        }
        self.challenges.append(new_challenge)
        self.save_challenges()

    def complete_challenge(self, challenge_id):
        if challenge_id not in self.completed_challenges:
            self.completed_challenges.add(challenge_id)
            print("Challenge marked as completed!")
        else:
            print("Challenge already completed.")

    def run(self):
        while True:
            self.display_challenges()
            print("\nOptions:")
            print("1. Add New Challenge")
            print("2. Complete Challenge")
            print("3. Exit")

            choice = input("Enter your choice (1/2/3): ")

            if choice == '1':
                title = input("Enter challenge title: ")
                description = input("Enter challenge description: ")
                self.add_challenge(title, description)
            elif choice == '2':
                challenge_id = int(input("Enter the challenge ID to mark as completed: "))
                self.complete_challenge(challenge_id)
            elif choice == '3':
                print("Exiting EcoPal App. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    eco_app = EcoPalLivingApp()
    eco_app.run()
