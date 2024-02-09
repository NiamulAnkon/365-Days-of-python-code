class Virtual_Wardrobe_managemnt_system:
    def __init__(self):
        self.profiles = []
        self.cloth_catageory = []
        self.cloths = []
    def usr_profile(self):
        self.name = input("Enter your name: ")
        self.password = input("Enter your password: ")
        self.usr_info = self.name, self.password
        self.profiles.append(self.usr_info)
    def main_menu(self):
        while True:
            usr_choice = int(input("1.Create a Wardrobe\n2.See Wardrobe\n3.add Cloths in wardrobe\n4.Exit\nEnter your choice: "))
            if usr_choice == 1:
                self.create_wardrobe()
            elif usr_choice == 2:
                self.see_wardrobe()
            elif usr_choice == 3:
                self.add_cloths()
            elif usr_choice == 4:
                print("GoodBye :)")
                break
    
    def create_wardrobe(self):
        self.wardrobe_name = input("Enter your wardrobe name: ")
        self.wardrobe_catageory = input("Enter your wardrobe catageory: ")
        self.wardrobe_season = input("Enter your Season: ")
        self.wardrobe_cloths = []
        self.wardrobe_info = self.wardrobe_name, self.wardrobe_catageory, self.wardrobe_season
        self.cloth_catageory.append(self.wardrobe_info)
    def See_Wardrobe(self):
        print(f"{self.wardrobe_info}")
    def add_cloths(self):
        self.cloth_catageorys = input("Enter your cloth catageory: ")
        self.cloths_season = input("Enter your cloth season: ")
        self.cloth_info = self.cloth_catageorys, self.cloths_season
        self.cloth_catageory.append(self.cloth_info)


if __name__ == "__main__":
    apps = Virtual_Wardrobe_managemnt_system()
    apps.usr_profile()
    apps.main_menu()
