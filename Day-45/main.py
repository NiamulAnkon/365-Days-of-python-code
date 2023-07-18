#Problem:
#Write a Python program that takes a string as input and returns the frequency count of each character in the string. The program should ignore spaces and be case-insensitive.
try:
    def char_frequency(string):
        frequency = {}
        for char in string.lower():
            if char != ' ':
                frequency[char] = frequency.get(char, 0) + 1
        return frequency

    #Example usage
    input_string = input("Enter a string: ")
    result = char_frequency(input_string)
    print(f"Character frequencies: {result}")
except ValueError:
    print("Something WentWrong")