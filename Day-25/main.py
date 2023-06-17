def calculator():
  """This function takes two numbers and an operator as input and
    performs the corresponding operation.
  """

  num1 = int(input("Enter the first number: "))
  """This line converts the input string to an integer.
  """

  num2 = int(input("Enter the second number: "))

  operation = input("Enter what you want to do (+,-,*,/): ")
  """This line gets the operator from the user.
  """

  opt = ["+", "-", "*", "/"]
  """This list stores the four possible operators.
  """

  if operation == opt[0]:
    """This if statement checks if the operator entered by the user is
      addition.
    """
    print("The addition is ", num1 + num2)
  elif operation == opt[1]:
    """This if statement checks if the operator entered by the user is
      subtraction.
    """
    print("The subtract is ", num1 - num2)
  elif operation == opt[2]:
    """This if statement checks if the operator entered by the user is
      multiplication.
    """
    print("The multiplication is ", num1 * num2)
  elif operation == opt[3]:
    """This if statement checks if the operator entered by the user is
      division.
    """
    print("This Division is ", num1 / num2)
  else:
    print("Something wrong")

try:
  """This try block executes the calculator function.
  """
  calculator()
except ValueError:
  """This except block catches the ValueError exception and
    print an error message.
  """
  print("Please put everything right")