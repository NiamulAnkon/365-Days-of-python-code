#Problem
#Write a Python program that takes a list of numbers as input and prints the sum of all the numbers in the list.

def list_number():
  """
  This function prompts the user to enter a list of numbers and then prints the sum of all the numbers in the list.

  Args:
    None

  Returns:
    None
  """

  # Prompt the user to enter a list of numbers
  numbers = input("Enter a list of numbers separated by spaces: ").split()

  # Convert the input string to a list of integers
  numbers = [int(num) for num in numbers]

  # Calculate the sum of the numbers
  sum_of_numbers = sum(numbers)

  # Print the result
  print("The sum of the numbers is:", sum_of_numbers)

try:
  # Call the list_number() function
  list_number()
except ValueError:
  # Print an error message if the user enters an invalid value
  print("Something went wrong")