#Problem
# Write a Python program that prompts the user to enter a string and prints the number of characters in the string.

def string():
  """
  This function prompts the user to enter a string and then calculates the number of characters in the string.

  Args:
    None

  Returns:
    None
  """

  # Prompt the user to enter a string
  string = input("Enter a string: ")

  # Calculate the number of characters in the string
  length = len(string)

  # Print the result
  print("The number of characters in the string is: ", length)

try:
  # Call the string() function
  string()
except ValueError:
  # Print an error message if the user enters an invalid value
  print("Something went wrong")