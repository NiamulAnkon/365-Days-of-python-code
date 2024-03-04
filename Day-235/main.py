#Problem: Write a Python function to check if a given number is prime or not.

def is_Prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        return True
    
num  = 17

if is_Prime(num):
    print(f"{num} is a Prikme number")

else:
    print(f"{num} is not a prime number")

