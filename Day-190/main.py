import random
import time

print("----Welcome To Hospital Management System")
time.sleep(10)


class Hospital_management_system:
    def __init__(self):
        self.pat_name = input("Enter your name patient: ")
        self.pat_age = int(input("Enter your patient age: "))
        self.pat_problem = input("Enter your patient disses: ")
        self.pat_info = [self.pat_name, self.pat_age, self.pat_problem]
        self.patient_cornf()
        self.patient_info_save()

    def patient_cornf(self):
        ward_number = ["1","2","3","4","5","6","7"]
        self.pat_ward_num = random.choice(ward_number)
        print("You have to pay 10,000$")
        time.sleep(5)
        self.pay = int(input("Pay: "))

        if self.pay == 10000:
            print("Your Patient is succesfully confrimed")
        elif self.pay < 10000:
            print("The Amount is too low try again")
        elif self.pay > 10000:
            print("The Amount is too high try again")
        else:
            print("Something went wrong")


    def patient_info_save(self):
        file_name = f"{self.pat_name}_info.txt"
        usr_info = f"{self.pat_info}\nWard_number: {self.pat_ward_num}"
        with open(file_name, "w") as file:
            file.write("".join(usr_info))

if __name__ == "__main__":
    app = Hospital_management_system()
