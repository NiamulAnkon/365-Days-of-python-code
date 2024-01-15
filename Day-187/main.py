import random
import time

print("-----Welcome to Buy Your Domain----")
time.sleep(10)
ip_for_domain = ["122.3.44.6.p","22.3312.5666.o","197.80.90","00ou22.22.o.22","86754.22.o"]

class Buy_Your_Domain:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        self.country = input("Enter your Country: ")
        self.buy_domain()
        self.save_usr_data()

    def buy_domain(self):
        self.domain_name = input("Enter your domain name")
        self.domain_ip = random.choice(ip_for_domain)
        print("Select your package for domain\n1. 1 Year - 1,000 \n2. 10 year- 10,000 \nLife time - 20,000")
        self.usr_select_package = int(input("Enter selected package (1-3): "))

        if self.usr_select_package == 1:
            print("Please wait for some time")
            time.sleep(20)
            pay = int(input("Pay: "))
            if pay == 1000:
                print("Congrats Your domain is succesfully created")
            else:
                print("Try again")
        elif self.usr_select_package == 2:
            print("Please wait for some time")
            time.sleep(20)
            pay = int(input("Pay: "))
            if pay == 10000:
                print("Congrats Your domain is succesfully created")
            else:
                print("Try again")
        elif self.usr_select_package == 3:
            print("Please wait for some time")
            time.sleep(20)
            pay = int(input("Pay: "))
            if pay == 20000:
                print("Congrats Your domain is succesfully created")
            else:
                print("Try again")
        else:
            print("Something went wrong try again")

    def save_usr_data(self):
        file_name = f"{self.domain_name}_info.txt"
        usr_data = f"User info:[{self.name, self.age, self.country}]\nDomain info: [{self.domain_name, self.domain_ip}]"
        with open(file_name, "w") as file:
            file.write("".join(usr_data))


if __name__ == "__main__":
    app = Buy_Your_Domain()
