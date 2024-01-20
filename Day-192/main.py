import time

print("----------Pet Shop----------")
time.sleep(5)

class Pet_Shop:
    def __init__(self):
        print("You have to register first")
        time.sleep(2)
        self.usr_name = input("Enter Your user name: ")
        self.usr_email = input("Enter your email: ")
        self.usr_password = input("Enter your password: ")
        self.usr_phbonenumber = int(input("Enter your Number: "))
        self.pet_menu()
        self.usr_info_for_buying()
        self.pet_items()
        self.save_data()

    def pet_menu(self):
        print("Welcome to Pet Menu")
        time.sleep(5)

        self.usr_pet_choice = input("Enter which type of pet you want (dog, cat, bird): ")
        self.usr_pet_choice_breed = input("Enter which breed of the pet you want: ")
        self.usr_pay = int(input("You have to pay 100$ pay it: "))
        print("wait for sometime")
        time.sleep(10)
        print("Congrats Your pet is ready now let's do the paperwork")

    def usr_info_for_buying(self):
        print("You have to do some confirmation to get your pet it's our policy")
        self.agree = input("Do You agree with the policy: ")
        if self.agree == "yes":
            print("Ok let's move on to the next step")
        elif self.agree == "no":
            print("Well you have to agree there is no choice")
        else:
            print("Something went wrong you have to type yes")

    def pet_items(self):
        print("We are going to give some staff for your pet so you have to sign your name in simple word agree")
        time.sleep(5)
        self.pet_staff_agree = input("1.Agree: ")

    def usr_feedback(self):
        print("Give us the review of your own opinion")
        self.opinion = input(": ")

    def save_data(self):
        file_name = f"{self.usr_name}_info.txt"
        usr_info = f"User information: {self.usr_name} {self.usr_password} {self.usr_phbonenumber}{self.usr_email}\nPet information: {self.usr_pet_choice}{self.usr_pet_choice_breed}\nThe amount of money paid: {self.usr_pay}\nTerms and condition: {self.pet_staff_agree} {self.agree}\nUser Opinion: {self.opinion}"
        with open(file_name, "w") as file:
            file.write("".join(usr_info))

if __name__ == "__main__":
    app = Pet_Shop()
