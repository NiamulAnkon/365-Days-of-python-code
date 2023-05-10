#Example of explicit typecasting:
string = "15"
number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum= number + string_number
print("The Sum of both the numbers is: ", sum)
a1 = "1"
b2 = "2"
#Python automatically converts
#a to int
a = 7
print(type(a))

#Python automatically converts b to float
b = 3.0
print(type(b))

#Python automatically converts c to float as it is a float addition
c = a + b
print(c)
print(type(c))

#it will give the value of 2 int numbrs
print(a + b)
#it will give the value of 2 stirng numbers
print(a1 + b2)
#it will convert sting into int and print the result of first print function
print(int(a1) + int(b2))

name = input("Enter your name: ")
print("Hi " + name)
con = input(name + " is it correct name you want type yes or no : ")
print("procces succesfull")