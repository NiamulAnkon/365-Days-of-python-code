#Exercise:Text-Based Adventure Game
class AdventureGame:
    def __init__(self, player_name):
        self.player_name = player_name
        self.current_room = "entrance"
        self.rooms = {
            "entrance": {
                "description": "You are at the entrance of a mysterious castle.",
                "north": "hallway",
                "east": "kitchen",
            },
            "hallway": {
                "description": "You are in a dimly lit hallway.",
                "south": "entrance",
                "west": "library",
            },
            "library": {
                "description": "You are in a dusty old library.",
                "east": "hallway",
            },
            "kitchen": {
                "description": "You are in a large kitchen with a dining table.",
                "west": "entrance",
                "east": "storeroom",
            },
           "storeroom": {
              "description": "Here is many thing but wait here is the key of the scerect room",
              "south": "Scerectroom"
            },
            "Scerectroom": {
              "description": "Here is the one pice you find it congrats",
              "west": "complete"
            },
            "complete": {
              "description": "Congrats you have completed the game type quit"
            },
        }

    def start_game(self):
        print(f"Welcome, {self.player_name}! Let's embark on an adventure.")
        self.explore_room()

    def move(self, direction):
        if direction in self.rooms[self.current_room]:
            self.current_room = self.rooms[self.current_room][direction]
            self.explore_room()
        else:
            print("You cannot go that way.")

    def explore_room(self):
        room = self.rooms[self.current_room]
        print(room["description"])
        print("Exits:", ", ".join(room.keys() - ["description"]))
        
    def quit_game(self):
        print("Thank you for playing. Goodbye!")


# Test the class
if __name__ == "__main__":
    player_name = input("Enter your name: ")
    game = AdventureGame(player_name)
    
    game.start_game()
    
    while True:
        command = input("Enter a command (move, explore, quit): ").lower()
        if command == "move":
            direction = input("Enter a direction (north, south, east, or west): ").lower()
            game.move(direction)
        elif command == "explore":
            game.explore_room()
        elif command == "quit":
            game.quit_game()
            break
        else:
            print("Invalid command. Try again.")