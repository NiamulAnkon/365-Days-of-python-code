print("-----Welcome to set drills app-----")


while True:
    usr_input = input("Enter your category for drills: ")

    usr_set_drills_num = int(input("Enter how maany drills you want to set (1-10): "))

    set_drills_num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    drills_list = []

    for i in range(usr_set_drills_num):
        drill = input(f"{i + 1}. ")
        drills_list.append(drill)

    file_name = f"{usr_input}_drills.txt"
    with open(file_name, "w") as file:
        file.write("\n".join(drills_list))

    print(f"Drills saved successfully in {file_name}")

    agn = input("wanna try another time? y/n: ")

    if agn == "y":
        continue
    elif agn == "n":
        print("Goodbye :)")
        break