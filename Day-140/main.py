import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

while True:
    def Track_number(number):

        ch_numbers = phonenumbers.parse(number, "CH")
        print(geocoder.description_for_number(ch_numbers, "en"))

        sp_numbers = phonenumbers.parse(number, "RO")
        print(carrier.name_for_number(sp_numbers, "en"))



    number = input("Enter your mobile number with country code: ")
    
    Track_number(number)

    usr_choice = input("Do you want to try again y/n: ")

    if usr_choice == "n":
        print("Goodbye")
        break
    elif usr_choice == "y":
        continue
    else:
        print("Something went wrong")
        break