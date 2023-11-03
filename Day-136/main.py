print("--------Welcome to server buy--------")
while True:
    server_name = input("Enter your name for server: ")
    readyornot = input("Are you ready to go y/n: ")

    if readyornot == "y":
        break
    elif readyornot == "n":
        continue
    else:
        break


def pay():
    pay_method = int(input("-----Which method you want------- \n1)Bkash 2)nagad \nChose which one: "))
    if pay_method == 1:
        print("Bakash on this number \n 01xxxxxxxxxxx")
        trx_id = input("Enter the trx id: ")
        print("Your server id address is "+ "www."+server_name+".com")
    elif pay_method == 2:
        print("Bakash on this number \n 01xxxxxxxxxxx")
        trx_id = input("Enter the trx id: ")
        print("Your server id address is "+ "www."+server_name+".com")
    else:
        print("Something went wrong")

pay()