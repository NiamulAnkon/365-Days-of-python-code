import random
class opd_ticket_managment:
    def __init__(self):
        self.patients = []
        self.patient_id = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17"]
        self.patient_info = []


    def main_menu(self):
        while True:
            admin_usr = int(input("1.Add patient\n2.Dellete patient\n3.See patients\n4.Exit\n: "))

            if admin_usr == 1:
                self.create_ticket()
            elif admin_usr == 2:
                self.dellete_patient()
            elif admin_usr == 3:
                self.see_patient()
            elif admin_usr == 4:
                print("Exiting....")
                break



    def create_ticket(self):
        pt_name = input("Emter the patient name: ")
        pt_age = int(input("Enter patient age: "))
        pt_gender = input("Enter patient gender: ")
        pt_visit_type = input("Enter the visit type (new patient, reserve patient, have apoitment): ")
        pt_date = int(input("Enter the date: "))
        pt_fee_type = input("Enter fee type: ")
        pt_room = int(input("enter the room number: "))
        pt_id = random.choice(self.patient_id)
        self.pt_info = pt_name, pt_age, pt_gender, pt_visit_type, pt_date, pt_fee_type, pt_room, pt_id
        self.patient_info.append(self.pt_info)
        self.patients.append(pt_name)
    
    def dellete_patient(self):
        pt_id = int(input("Enter patient id: "))

        if pt_id in self.patient_id:
            self.patients.remove(self.pt_info)
        else:
            print("Something went wrong")
    def see_patient(self):
        print(f"Patients:\n{self.patient_info}\n")
    def usr_info(self):
        file_name = f"Patient_info.txt"
        with open(file_name, "w") as file:
            file.write("".join(self.patient_info))

if __name__ == "__main__":
    app = opd_ticket_managment()
    app.main_menu()