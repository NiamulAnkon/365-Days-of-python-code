#Problem:
#Write a Python program that takes a string as input and counts the number of vowels (a, e, i, o, u) present in the string. The program should be case-insensitive.
def count_vowels(string):
    """
    This function takes a string as input and counts the number of vowels present in the string.

    Args:
        string (str): The input string.

    Returns:
        int: The number of vowels in the string.
    """

    vowels = "aeiou"
    count = 0

    for char in string.lower():
        if char in vowels:
            count += 1

    return count

try:
    string = input("Enter a word or phrase: ")
    if not string.strip():
        raise ValueError("Input cannot be empty or contain only whitespace.")
    result = count_vowels(string)
    print("Number of vowels:", result)
except ValueError as e:
    print("Invalid input:", str(e))
except Exception as e:
    print("Something went wrong:", str(e))
