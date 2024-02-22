import time
class Hacker_game:
    def __init__(self):
        self.tasks = ["Hack this id john@gmail.com ", "Make a phising link ", "hack this id Rayan Billi"]
        self.completed_task = []
        self.component = ["Laptop-Kali Linux", "android phone"]
        self.rank = 1000
        self.money = 0

    def signup(self):
        self.user_name = input("Enter your username: ")
        self.passwod = input("Chose a password: ")
    
    def main_menu(self):
        while True:
            print(f"Welcome {self.user_name} do tasks to rank up and get money to buy component and other things\n")
            usr_chs = int(input("1.Tasks\n2.Completed Tasks\n3.Rank\n4.Money\n5.Buy Component\n6.See Component\n7.Do Tasks\n8.Exit\nChose your option: "))

            if usr_chs == 1:
                self.show_taks()
            elif usr_chs == 2:
                self.completed_task()
            elif usr_chs == 3:
                self.rank()
            elif usr_chs == 4:
                self.show_money()
            elif usr_chs == 5:
                self.buy_component()
            elif usr_chs == 6:
                self.see_component()
            elif usr_chs == 7:
                self.do_tasks()
            elif usr_chs == 8:
                print("GoodBye :)")
                break
            else:
                print("Something went wrong try again")
                continue
                
    def show_taks(self):
        print(f"Tasks you have is: {self.tasks}")
    def completed_task(self):
        print(f"You have completed this tasks\n{self.completed_task}")
    def rank(self):
        print(f"Your rank is {self.rank}")
    def show_money(self):
        print(f"You have {self.money}$")
    def buy_component(self):
        while True:
            comp = ["Desktop-Kali-linux", "Mac Book Pro", "Laptop- for professional Hacker"]
            chs_component = int(input("1.Desktop-Kali-linux- 100$\n2.Mac Book Pro- 500$\n3.Laptop- for professional Hacker- 1000$"))
            if chs_component == 1:
                pay = int("Do you want to checkout y/n: ")
                self.money -= 100
                self.component.append(comp[0])
            if chs_component == 2:
                pay = int("Do you want to checkout y/n: ")
                self.money -= 500
                self.component.append(comp[1])
            if chs_component == 3:
                pay = int("Do you want to checkout y/n: ")
                self.money -= 1000
                self.component.append(comp[2])
            else:
                print("Something Went wrong")
                break
    def see_component(self):
        print(f"The Component {self.component}")
    def do_tasks(self):
        self.need_comp_task = ["Sudo Hack john@gmail.com", "sudo phising", "Sudo Hack Rayan Billi"]
        self.task_money = 50
        print("For hacking use this command:Sudo Hack mail or username\nfor phising link- sudo phising type any name\n")
        usr_choice = input("Enter what you want to do type the line of code: ")
        if usr_choice in self.need_comp_task:
            print("Processing...")
            time.sleep(15)
            print("\nCongrats your task is completed")
            self.completed_task.append(self.usr_choice)
            self.task_money += self.money
            self.task_money -= self.rank
        else:
            print("Something went wrong")
            
if __name__ == "__main__":
    game = Hacker_game()
    game.signup()
    game.main_menu()