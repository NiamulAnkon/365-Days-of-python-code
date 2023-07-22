#Exercise:
#Calculate the AverageWrite a Python function called calculate_average that takes a list of numbers as input and returns the average of those numbers.

def calculate_average_numbers(number):
    total = sum(number)
    average = total / len(number)
    return average
try:
    # Test the function
    numbers_list = [3,6,34,24,5,6,3,1,9]
    result = calculate_average_numbers(numbers_list)
    print(f"The average number is : {result}")
except ValueError or IndexError:
    print("Something Went Wrong")