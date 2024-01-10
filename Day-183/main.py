#import area
import time

#welcome area
print("-----WelCome To register for Rubik's Cube Comp-----")
time.sleep(5)

#usr_info area
usr_name = input("Enter your name: ")
usr_age = int(input("Enter your age: "))
usr_country = input("Enter your country: ")
usr_info_for_reg = [usr_name, usr_age, usr_country]

print(f"Your Info is:\n{usr_info_for_reg}")
time.sleep(10)
#loop area with function
while True:
    def set_fo_rubik():
        print("On Which event you want to participate \n\n")
        print("1.3x3\n2.2x2\n3.4x4\n4.5x5")


        usr_choice = int(input("Enter your choice (1-4): "))

        if usr_choice == 1:
            print("wait for response")
            time.sleep(20)
            print("Congrats you are elegible")

        elif usr_choice == 2:
            print("wait for response")
            time.sleep(20)
            print("Congrats you are elegible")

        elif usr_choice == 3:
            print("wait for response")
            time.sleep(20)
            print("Congrats you are elegible")

        elif usr_choice == 4:
            print("wait for response")
            time.sleep(20)
            print("Congrats you are elegible")
        else:
             print("try again")
    set_fo_rubik()


    chs_again = input("want to participate more event y/n: ")

    if chs_again == "y":
            time.sleep(5)
            continue
    elif chs_again == "n":
            time.sleep(5)
            print("GoodBye :)")
            break
    else:
            print("try again")
            time.sleep(30)
            break    

#saving all the usr_info
usr_full_info = [usr_info_for_reg]
file_name = "Your_Info.txt"
with open(file_name, "w") as file:
    file.write("".join(str(usr_full_info)))
print(f"Your Info is saved in: {file_name}")
