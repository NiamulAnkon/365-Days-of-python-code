try:
    def list():
        vplist = ["100vp = 200bdt", "500vp = 1000bdt", "1000vp = 1500bdt", "1500vp = 2000bdt", "5000vp = 5500bdt"]
        print(vplist)
    list()
    def p_info():
        riot_id = input("Enter the riot id: ")
        tagline = input("Enter the tagline: ")
        print(f"Your account name is {riot_id}\n Your Tagline is {tagline}")
    p_info()
    vpamount = int(input("Enter the amount of vp: "))
    moneyamount = int(input("Enter the amount of money: "))
    if(vpamount >= moneyamount):
     print("not enough money")
    else:
        print("Thanks for Buying")

    def refund():
        refund = input("OR You missed buy your vp do you want refund y/n: ")
        if(refund == "y" or refund == "yes"):
            print("Your refund is completed")
        else:
            print("Thanks for sured us")
    refund()
except ValueError:
    print("Something went wrong try again")