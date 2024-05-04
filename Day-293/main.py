#Problem
# Exercise 2: Print the sum of the current number and the previous number
# Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

# Expected Output:

# Printing current and previous number sum in a range(10)
# Current Number 0 Previous Number  0  Sum:  0
# Current Number 1 Previous Number  0  Sum:  1
# Current Number 2 Previous Number  1  Sum:  3
# Current Number 3 Previous Number  2  Sum:  5
# Current Number 4 Previous Number  3  Sum:  7
# Current Number 5 Previous Number  4  Sum:  9
# Current Number 6 Previous Number  5  Sum:  11
# Current Number 7 Previous Number  6  Sum:  13
# Current Number 8 Previous Number  7  Sum:  15
# Current Number 9 Previous Number  8  Sum:  17

previus_num = 0

print("Printing current and previous number sum in a range(10)")

for i in range(previus_num, 10):
    current_num = i
    sum_ = i+previus_num
    previus_num = i
    print(f"Current Number: {current_num} Previous Number: {previus_num} : Sum :  {sum_}")

