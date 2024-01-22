print("-------Welcome to create your anime list for watching------")

class Anime_list_for_Watching:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        self.anime_list = []

    def anime_list(self):
        anime_names = input("Enter your anime names: ")
        self.anime_list.append(anime_names)

    def usr_choice(self):
        while True:
            choice = int(input("1. Add Anime\n2. See Anime List\n3. Exit"))
            if choice == 1:
                anime_names2 = input("Enter your anime names:")
                self.anime_list.append(anime_names2)
            elif choice == 2:
                print(self.anime_list)
            elif choice == 3:
                print("Goodbye :)")
                self.save_data()
                break
            else:
                print("Something went wrong, try again")

    def save_data(self):
        file_name = f"{self.name}_anime_info.txt"
        usr_info = f"User info: {self.name} {self.age}\nAnime list: {self.anime_list}"
        with open(file_name, "w") as file:
            file.write(usr_info)

if __name__ == "__main__":
    app = Anime_list_for_Watching()
    app.usr_choice()