import time
import random
print("----------Welcome to movers app----------")
time.sleep(5)

class Movers_App:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.email = input("Enter your email: ")
        self.phone_number = int(input("Enter your phoneNumber: "))
        self.password = input("Enter your password: ")
        self.service_option()
        self.service_request()
        self.payment()
        self.save_data()


    def service_option(self):
        self.service_list = ["1.residential moves", "2.commercial moves", "3.packing service", "4.storage service"]
        print(f"Our Services are \n{self.service_list}")
        self.usr_choice = int(input("Which service you want to chose (1-4): "))


    def service_request(self):
        self.moving_date = int(input("Enter when you want to shift: "))
        self.current_location = input("Enter your location: ")
        self.destination = input("Enter your destination: ")

    def payment(self):
        print("You have to pay 1,000$ \nbut you have to pay 500$ in advance")
        self.pay = int(input("Pay: "))

    def save_data(self):
        file_name = f"{self.name}_info.txt"
        user_data = f"User Information: {self.name} {self.email} {self.phone_number} {self.password} \nService Information: {self.usr_choice} {self.moving_date} {self.current_location} {self.destination}"
        with open(file_name, "w") as file:
            file.write("".join(user_data))


if __name__ == "__main__":
    app = Movers_App()