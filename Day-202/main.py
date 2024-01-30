class Assassin_Game:
    def __init__(self):
        self.missions = ["1.Steal Painting" "2.Kill Mafia", "3.Kill ruby owner"]
        self.account = []
        self.levle = 1
        self.logged_accounts = None

    def how_to_play(self):
        print("How To Play:")
        print("In this game, you will take on the role of an assassin and complete various missions.")
        print("Earn points by successfully completing missions and level up to unlock new challenges.")

    def about(self):
        print("About:")
        print("Assassin Game is a text-based adventure where you become an assassin and take on different missions.")
        print("Developed by [Your Name].")

    def see_missions(self):
        print("Available Missions:")
        for mission in self.missions:
            print(mission)

    def complete_mission(self):
        self.see_missions()
        mission_choice = int(input("Enter the mission number you want to complete: "))

        if 1 <= mission_choice <= len(self.missions):
            print(f"Mission {mission_choice} completed successfully!")
            self.levle += 1
            print(f"You leveled up to Level {self.levle}")
        else:
            print("Invalid mission number. Try again.")

    def watch_info(self):
        print("Your Account Information:")
        print(f"Username: {self.logged_accounts['username']}")
        print(f"Level: {self.levle}")

    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        for account in self.account:
            if account['username'] == username and account['password'] == password:
                print(f"Welcome back, {username}!")
                self.logged_accounts = account
                return True

        print("Invalid username or password. Please try again.")
        return False

    def main_menu(self):
        while True:
            usr_choice = int(input("Main Menu \n1.Start New Game\n2.How To Play\n3.About \n4.Exit"))
            if usr_choice == 1:
                self.new_game()
            elif usr_choice == 2:
                self.how_to_play()
            elif usr_choice == 3:
                self.about()
            elif usr_choice == 4:
                print("GoodBye")
                break
            else:
                print("Try again")
                continue

            while self.logged_accounts:
                game_choice = int(input("Game Menu \n1.See Missions\n2.Complete Mission\n3.Watch My Info\n4.Logout"))
                if game_choice == 1:
                    self.see_missions()
                elif game_choice == 2:
                    self.complete_mission()
                elif game_choice == 3:
                    self.watch_info()
                elif game_choice == 4:
                    print("Logging out...")
                    self.logged_accounts = None
                    break
                else:
                    print("Invalid choice. Try again.")

if __name__ == "__main__":
    gameofassasin = Assassin_Game()
    gameofassasin.main_menu()