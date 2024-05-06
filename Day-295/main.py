# Exercise 5: Display numbers from a list using loop
# Write a program to display only those numbers from a list that satisfy the following conditions

# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop
# Given:

# numbers = [12, 75, 150, 180, 145, 525, 50]
# Expected output:

# 75
# 150
# 145

# Exercise 6: Count the total number of digits in a number
# Write a program to count the total number of digits in a number using a while loop.

# For example, the number is 75869, so the output should be 5.
def dn(numbers):
    for i in numbers:
        if i > 500:
            break
        elif i > 150:
            continue
        elif i % 5 == 0:
            print(i)
numbers = [12, 75, 150, 180, 145, 525, 50]
dn(numbers)

def count_the_number():
    numbers  = 75869
    counter = 0
    while numbers != 0:
        numbers = numbers // 10
        counter = counter + 1
    return counter

print(count_the_number())
