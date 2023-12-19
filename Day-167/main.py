print("----------Welcome to Trading site---------- \n\n")

while True:
    usr_choice = int(input("What you want to do:\n1|Create account\n2|Buy Crypto\n3|Add Money\n4|Withdraw\n5|trade with someone \n6|Sell Crypto\n7|Check Balance \n8|Exit\n:"))

    balance = 1000

    if usr_choice == 1:
        name = input("Enter your name: ")
        phone = int(input("Enter your phone number: "))
        age = int(input("Enter your age: "))

        if age < 18:
            print("You are not eligible for this site")
        elif age >= 18:
            print(f"You are account is ready to go \nAccount Details: \n name: {name} \n Phone: {phone}\n Age: {age}")
            continue

    elif usr_choice == 2:
        chs_crp = input("Which type of crypto you want to buy (bitcoin, dogecoin, usdcoin, cardano):  \n\n")
        if chs_crp == "bitcoin":
            print("The Price of the Bitcoin is 500$ \npay the 500$ to buy this bitcoin")
            pay_btn = int(input("Pay for it: "))
            balance -= pay_btn
            print("You have successfully bought Bitcoin")
            print(f"Your balance is: {balance}")
        elif chs_crp == "dogecoin":
            print("The Price of the dogecoin is 300$ \npay the 300$ to buy this dogecoin")
            pay_btn = int(input("Pay for it: "))
            balance -= pay_btn
            print("You have successfully bought Dogecoin")
            print(f"Your balance is: {balance}")
        elif chs_crp == "usdcoin":
            print("The Price of the usdcoin is 400$ \npay the 400$ to buy this usdcoin")
            pay_btn = int(input("Pay for it"))
            balance -= pay_btn
            print(f"Your balance is: {balance}")
        elif chs_crp == "cardano":
            print("The Price of the cardano is 199$ \npay the 199$ to buy this cardano")
            pay_btn = int(input("Pay for it: "))
            print("You have successfully bought Cardano")
            balance -= pay_btn
            print(f"Your balance is: {balance}")


    elif usr_choice == 3:
        money_amount = int(input("Enter how much money you want ot add: "))
        money_amount + balance
        print(f"\n\nYour Balance is: {balance}")
    elif usr_choice == 4:
        withdraw_amount = int(input("Enter how much money you want to withdraw: "))
        balance -= withdraw_amount
        print(f"Your balance is: {balance}")
        if withdraw_amount > balance:
            print("Your balance is too low")
        elif withdraw_amount <= balance:
            print("Withdraw is done :)")

    elif usr_choice == 5:
        ano_usr_name = input("Enter the user name that you want to treade with: ")

        trade_thing = input("Enter waht you want to trade with him e.g(bitcoin, usdcoin): ")
        print("Your Trade is succesfully done \n---------------------")

    elif usr_choice == 6:
        crypto_details = input("Which crypto you want ot sell: ")
        sell_price = int(input("Enter for how much price you want to sell: "))
        print("Your Crypto is succesfully sell\n\n")
        current_balance = sell_price + balance
        print(f"Your Current Balance: {balance}")

    elif usr_choice == 7:
        print(f"Your balance is: {balance}")

    elif usr_choice == 8:
        print("GoodBye :)")
        break
