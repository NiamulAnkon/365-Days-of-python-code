class FitnessChallengeTracker:
    def __init__(self):
        self.users = {}
        self.challenges = {}

    def register_user(self, username, password):
        if username not in self.users:
            self.users[username] = {'password': password, 'challenges_completed': {}}
            print(f"User '{username}' registered successfully!")
        else:
            print("Username already exists. Please choose a different username.")

    def create_challenge(self, challenge_name, duration_days, goal):
        challenge_id = len(self.challenges) + 1
        self.challenges[challenge_id] = {'name': challenge_name, 'duration': duration_days, 'goal': goal, 'participants': {}}
        print(f"Challenge '{challenge_name}' created successfully!")

    def join_challenge(self, username, challenge_id):
        if username in self.users and challenge_id in self.challenges:
            if username not in self.challenges[challenge_id]['participants']:
                self.challenges[challenge_id]['participants'][username] = 0
                print(f"User '{username}' joined challenge '{self.challenges[challenge_id]['name']}'!")
            else:
                print(f"User '{username}' is already participating in this challenge.")
        else:
            print("Invalid username or challenge ID.")

    def record_progress(self, username, challenge_id, progress):
        if username in self.users and challenge_id in self.challenges:
            if username in self.challenges[challenge_id]['participants']:
                self.challenges[challenge_id]['participants'][username] += progress
                print(f"Progress recorded for user '{username}' in challenge '{self.challenges[challenge_id]['name']}'!")
            else:
                print(f"User '{username}' is not participating in this challenge.")
        else:
            print("Invalid username or challenge ID.")

    def display_leaderboard(self, challenge_id):
        if challenge_id in self.challenges:
            challenge = self.challenges[challenge_id]
            sorted_participants = sorted(challenge['participants'].items(), key=lambda x: x[1], reverse=True)
            print(f"Leaderboard for challenge '{challenge['name']}':")
            for rank, (username, progress) in enumerate(sorted_participants, start=1):
                print(f"{rank}. {username}: {progress}")
        else:
            print("Invalid challenge ID.")


# Example Usage:
tracker = FitnessChallengeTracker()

# Register users
tracker.register_user("user1", "password1")
tracker.register_user("user2", "password2")

# Create challenges
tracker.create_challenge("Steps Challenge", 7, 10000)
tracker.create_challenge("Running Challenge", 14, 50)

# Join challenges
tracker.join_challenge("user1", 1)
tracker.join_challenge("user2", 1)
tracker.join_challenge("user2", 2)

# Record progress
tracker.record_progress("user1", 1, 8000)
tracker.record_progress("user2", 1, 9000)
tracker.record_progress("user2", 2, 40)

# Display leaderboard
tracker.display_leaderboard(1)
tracker.display_leaderboard(2)
