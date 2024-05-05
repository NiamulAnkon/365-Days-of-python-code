# Exercise 1: Print First 10 natural numbers using while loop

# Expected output:

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# Exercise 2: Print the following pattern
# Write a program to print the following number pattern using a loop.

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

# Exercise 3: Calculate the sum of all numbers from 1 to a given number
# Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

# For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)

# Expected Output:

# Enter number 10
# Sum is:  55

# Exercise 4: Write a program to print multiplication table of a given number
# For example, num = 2 so the output should be

# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20

for i in range(10):
    print(i+1)


row  = 5
for i in range(1, row + 1, 1):
    for j in range(1, i + 1):
        print(j, end=' ')

    print("")


usr_chs = int(input(": "))
s = sum(range(1), usr_chs + 1)
print(s)


n = 2
for i in range(1, 10):
    i = i + 1
    p = i * n
    print(p)


