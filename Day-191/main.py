import time
import random

print("-----Welcome to create your Football club------")
time.sleep(5)


class Creat_football_club:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        self.bal = int(input("Enter how much money you want to add to your account for your club: "))
        self.creat_your_club()
        self.chose_players_for_your_club()
        self.Save_usr_data()

    def creat_your_club(self):
        self.sponser = ["Punma","Nike","Adidas"]
        self.sponser_money = ["100,000,000$", "50,00,000$","76,00,000$"]
        self.club_name = input("Enter your Club name: ")
        self.club_bal = int(input("Enter how much money will have in your club: "))
        self.club_sponser = random.choice(self.sponser)
        self.club_sponser_moeny_offerd = random.choice(self.sponser_money)
        print(f"A Company is going to sponser you. The company name is {self.club_sponser} and they are offering {self.club_sponser_moeny_offerd}$")
        time.sleep(5)

    def chose_players_for_your_club(self):
        print(f"{self.name}, boss we are setting the formation by default ----> 4-3-3 <-----\nand sorry you can't change that because the coder is so lazy to add more")
        time.sleep(10)
        self.chs_strikers = input("Chose your 3 strikers (eg.neymar,messi,ronaldo): ")
        self.chs_midfilder = input("Chose yur 3 Midfilders: ")
        self.chs_defender = input("Chose your 4 difender: ")
        self.chs_goalkeeper = input("Chose your Golkeeper: ")
        self.chs_manager = input("Chose your Manager: ")
        print("Congrats you Club Created Succesfully")

    def Save_usr_data(self):
        file_name = f"{self.name}_info.txt"
        usr_info = f"The Boss info: {self.name}, {self.age}, {self.bal} \nThe club info: {self.club_name}, {self.club_bal}, {self.club_sponser}, {self.club_sponser_moeny_offerd}\nClub Player and Manager info: Strikers: {self.chs_strikers} Midfielders: {self.chs_midfilder} Difender: {self.chs_defender} Goalkeeper: {self.chs_goalkeeper} Manager: {self.chs_manager}"
        with open(file_name, "w") as file:
            file.write(''.join(usr_info))

if __name__ == "__main__":
    club = Creat_football_club()
    
