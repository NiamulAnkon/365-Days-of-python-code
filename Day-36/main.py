# #Problem
# #Write a Python program that takes a list of numbers as input and returns the sum of all the even numbers in the list.

def sum_of_even_numbers(numbers):
  """
  This function takes a list of numbers as input and returns the sum of all the even numbers in the list.

  Args:
    numbers (list): A list of integers.

  Returns:
    int: The sum of all the even numbers in the list.
  """

  # Initialize a variable to store the sum of the even numbers.
  total_sum = 0

  # Iterate through the list of numbers.
  for num in numbers:

    # Check if the number is an integer and even.
    if isinstance(num, int) and num % 2 == 0:

      # Add the number to the sum.
      total_sum += num

  # Return the sum of the even numbers.
  return total_sum

# Example usage
numbers = [1,2,3,4,5,6,7,8,9] 
result = sum_of_even_numbers(numbers)
print("Sum of even numbers:", result)