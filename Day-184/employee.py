import time
import random

def employe_login():
    ids = ["9375","0175","0925"]
    emp_name = input("Enter your name: ")
    emp_age = int(input("Enter your age: "))
    emp_country = input("Enter your country: ")
    emp_id = random.choice(ids)
    emp_info = emp_name, emp_age, emp_country, emp_id

    time.sleep(2)

    file_name = "employe_information.txt"
    with open(file_name, "w") as file:
        file.write("".join(str(emp_info)))

employe_login()

def emp_work():
    emp_choice = int(input("Enter your choice\n1.Find customer\n2.Exit: "))

    if emp_choice == 1:
        print("Finding someone")
        time.sleep(20)
        print(f"finded someone who want to go somewhere")
        emp_yes_no = int(input("Do you want to continue with this customer:\n1.yes\n2.no: "))

        if emp_yes_no == 1:
            print("Please wait for response")
            time.sleep(10)
            print("Yes, Everything done correctly you can go")
        elif emp_yes_no == 2:
            print("wait for deny")
            time.sleep(5)
            print("The trip is succesfully denied")
        else:
            print("Something went wrong")
    if emp_choice == 2:
        print("Goodbye")
    else:
        print("Something went wrong")


emp_work()
