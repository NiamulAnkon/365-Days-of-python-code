#Problem:
#Write a Python program that takes a string as input and checks if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, disregarding spaces, punctuation, and capitalization.
try:
    def palindrome(string):
        string = ''.join(e for e in string if e.isalnum()).lower()
        return string == string[::-1]

    # Example usage
    input_string = input("Enter a string: ")
    if palindrome(input_string):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
except ValueError:
    print("Something went wrong")
