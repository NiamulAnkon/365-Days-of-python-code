#Password Genarator
import random #2
import string #2
try:
    def password():
        # Define the length and complexity of the password
        length = int(input("Enter the len of password: "))#i Updated -5
        complexity = "medium" #2

        # Define the possible characters for each complexity level
        low_complexity = string.ascii_letters #3
        medium_complexity = string.ascii_letters + string.digits #2
        high_complexity = string.ascii_letters + string.digits + string.punctuation #2

        # Choose the set of characters based on the desired complexity
        if complexity == "low": #2
            characters = low_complexity #1
        elif complexity == "medium": #1
            characters = medium_complexity #1
        elif complexity == "high": #1
            characters = high_complexity #1

        # Generate the password
        password = ''.join(random.choice(characters) for i in range(length)) #2

        # Print the password
        print("Your password is: ", password) #1
    password()
except ValueError:
    print("Something went wrong")