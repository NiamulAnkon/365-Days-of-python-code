import time
import random
print("------Welocome to Car Showroom------")
time.sleep(5)


class Car_showroom:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        self.email = input("Enter your email: ")
        self.phone_number = int(input("Enter your phone number: "))
        self.location = input("Enter your location: ")

    def cars(self):
        self.cars_brands = ["Toyota", "Mustang", "Hyundai", "ferrari", "Lamborginhi", "Buggati"]
        self.cars_prices = ["90,0000,000", "180,0000,000","60,00,000", "190,0000,000", "200,0000,000", "250,0000,000"]
    def user_choices(self):
        while True:
            self.usr_choice = int(input("1.Buy car\n2.Sell Car\n3.exit\n: "))

            if self.usr_choice == 1:
                self.chose_car = input("Chose your car model: ")
                if self.chose_car in self.cars_brands:
                    print(f"So your chosing {self.chose_car}\nSo You have to pay {random.choice(self.cars_prices)}")
                    self.pay = int(input("Pay: "))

            elif self.usr_choice == 2:
                self.sell_car = input("Enter your car model for sale: ")
                self.sell_car_price = int(input("Enter your price for car: "))
                print(f"So We found someone who want to buy you car and he will give you all the money and we have sold it\nCongrats you will get your money now")

            elif self.usr_choice == 3:
                print("GoodBye :)")
                break
            else:
                print("Something went wrong")
                continue
    def save_data(self):
        file_name = f"{self.name}_info.txt"
        usr_info = f"User Information: {self.name}, {self.age}, {self.email}, {self.phone_number}\nCar Information: {self.chose_car}, {self.pay}\nCar Sell Information: {self.sell_car}, {self.sell_car_price}"
        with open(file_name, "w") as file:
            file.write("".join(usr_info))

if __name__ == "__main__":
    app = Car_showroom()
    app.user_choices()

