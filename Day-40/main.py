import random
def account():
  name = input("Enter your name for card: ")
  age = int(input("Enter your age: "))
  set_a_pin = int(input("Enter 4 digit pin: "))
  cvv = int(input("Enter the 3 digit cvv: "))
  balance = int(input("Enter how much money you want to add on your account: "))
  available_numbers = ["7547,9264,6392,6340", "5284,8164,9631,7342", "0143,1094,5245,0173"]
  card_number = random.choice(available_numbers)
  print(f"Your card information \n Name: {name} \n Age: {age} \n Pin: {set_a_pin} \n CVV: {cvv} \n CardNumber: {card_number} \n Balance: {balance}")
  
account()