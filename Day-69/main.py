#Problem: Bank Account Management
class BankAccount:
  def __init__(self, account_number, account_holder, initial_balance):
    self.account_number = account_number
    self.account_holder = account_holder
    self.initial_balance = initial_balance
  def deposit(self, amount):
    if amount > 0:
      self.initial_balance += amount
      return True
    return False
  def withdraw(self, amount):
    if 0 < amount <= self.initial_balance:
      self.initial_balance -= amount

  def get_balance(self):
    return self.initial_balance

account1 = BankAccount("89249235", "ANKON", 500000)

account1.deposit(500)
account1.withdraw(200)

print(f"The Account Holder is: {account1.account_holder}")
print(f"The Account Number is: {account1.account_number}")
print(f"Current Balance is: {account1.get_balance()}")

if not account1.withdraw(500000):
  print("Withdraw faield: not enough balance")

if not account1.deposit(-100):
  print("Deposit failed: Invalid amount")