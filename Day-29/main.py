try:
    def kbc():
        welcome = "Welcome to KBC"
        print(welcome.center(50,'.'))

        qustions = ["1.Which on is the correct answer?","a)I am a Gamer., b)I am a Coder."]
        print(qustions[0])
        print(qustions[1])
        print("chose the answear")
        opt = ["a","b"]
        ans = input("Enter the Correct option: ")
        if(ans == opt[1]):
            print("Congrats you win a 100$")
        else:
            print("Sorry you missed the pirce of 100$ :(")
        qustions2 = ["2. Which one is the best in 2021?","a)Minecraft, b)Roblox"]
        print(qustions2[0])
        print(qustions2[1])
        opt2 = ["a,b"]
        ans = input("Chose the answear: ")
        if(ans == opt[0]):
            print("Congrats you win a 200$")
        else:
            print("Sorry you missed the pirce of 200$ :(")
        qustions2 = ["3. is it true the def keyword use for define a function in python ?","a)Yes, b)No"]
        print(qustions2[0])
        print(qustions2[1])
        opt2 = ["a,b"]
        ans = input("Chose the answear: ")
        if(ans == opt[0]):
            print("Congrats you win a 300$")
        else:
            print("Sorry you missed the pirce of 300$ :(")

    kbc()
except:
    print("Something went wrong try again")