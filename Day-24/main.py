#Problem:
# Write a program that asks the user to enter their age and prints out a message stating whether they are old enough to vote (18 years or older) or not.

#solution

try:

    def ageforvote():
        age = int(input("Enter your age: "))

        if(age < 18):
            print(f"Your age is {age} sorry you can't vote")
        elif(age >= 18):
            print(f"Your age is {age} you can vote")
        else:
            print("Something went wrong")

    ageforvote()
except ValueError:
    print("Something went wrong")