print("-----Welcome to my personal portfolio-----")


class Personal_Portfolio:
    def dasboard(self):
        while True:
            self.usr_choice = int(input("1.Home\n2.About\n3.Projects\n4.Exit"))
            if self.usr_choice == 1:
                print("Well i dont know what to do here so sorry")
            elif self.usr_choice == 2:
                about = "Hello, \nMy name is MD Niamul Islam Ankon\ni read in class 7 and i am a intermidiate python develper and i have done web developement"
                print(f"About me: \n{about}")
            elif self.usr_choice == 3:
                projects = ["School management system", "bank management system"]
                print(f"My Projects:\n{projects}")
            elif self.usr_choice == 4:
                print("Goodbye")
                break
            else:
                print("Something went wrong")

if __name__ == "__main__":
    personal_portfolio = Personal_Portfolio()
    personal_portfolio.dasboard()