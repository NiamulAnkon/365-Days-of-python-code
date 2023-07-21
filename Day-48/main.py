#exercise
# Find the Largest Number
# Write a Python function called find_largest_number that takes a list of numbers as input and returns the largest number from the list.

def find_largest_number(number):
    largest = number[0]
    for num in number:
        if num > largest:
            largest = num
    return largest

try:
    # Test the function
    number_list = [2,7,4,9,1,2,0,2,]
    result = find_largest_number(number_list)
    print(f"The Largest number is: {result}")
except:
    print("Something Went Wrong")