#Problem:
#Write a Python program that takes a list of numbers as input and returns a new list with only the unique numbers from the original list, preserving their original order.
def get_unique_numbers(numbers):
  """
  This function takes a list of numbers as input and returns a list of unique numbers.

  Args:
    numbers (list): A list of numbers.

  Returns:
    list: A list of unique numbers.
  """

  # Initialize a list to store the unique numbers.
  unique_numbers = []

  # Iterate through the list of numbers.
  for num in numbers:

    # Check if the number is not already in the list of unique numbers.
    if num not in unique_numbers:

      # Add the number to the list of unique numbers.
      unique_numbers.append(num)

  # Return the list of unique numbers.
  return unique_numbers

# Example usage
numbers = [1, 2, 3, 4, 2, 3, 5, 6, 1]
result = get_unique_numbers(numbers)
print("Unique numbers:", result)
