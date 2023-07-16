#Problem
#Write a Python program that takes a list of strings as input and returns a new list containing only the strings that have a length greater than 5.

def filterlongstring(string):
    long_STRING = []
    for string in string:
        if len(string) > 5:
            long_STRING.append(string)
    return long_STRING
    
# Example usage
strings = ['apple', 'banana', 'grapefruit', 'orange', 'kiwi']
result = filterlongstring(strings)
print("Long strings:", result)