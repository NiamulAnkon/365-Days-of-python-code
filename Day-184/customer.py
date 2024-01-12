import time

print("-----Welcome to book your cab-----")
time.sleep(5)

def login_signin():
    usr_name = input("Enter your name: ")
    usr_age = int(input("Enter your age: "))
    usr_country = input("Enter your country: ")
    usr_info = usr_name, usr_age, usr_country

    time.sleep(2)

    file_name = "user_information.txt"
    with open(file_name, "w") as file:
        file.write("".join(str(usr_info)))

login_signin()

def book_your_cab():
    usr_choice = int(input("Enter what you want to do \n1.book a cab\n2.exit: "))
    time.sleep(3)

    if usr_choice == 1:
        print("-----Chose your location from - to-----")
        usr_from = input("From: ")
        time.sleep(2)
        usr_to = input("To: ")
        time.sleep(2)
        print(f"So you are going from {usr_from} to {usr_to} so now you have to 500$")
        time.sleep(5)
        pay = int(input("Pay 500$ by typing it: "))

        if pay == 500:
            print("Congrats your cab is booked correctly")
        elif pay < 500:
            print("Your amount is too low try again")
        elif pay > 500:
            print("Your amount is too high")
        else:
            print("Something went wrong")

    elif usr_choice == 2:
        print("Good Bye")

    else:
        print("Something went wrong")

book_your_cab()
