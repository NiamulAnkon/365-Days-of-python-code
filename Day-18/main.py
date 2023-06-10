#Local and Global Variables

x = 4
print(x)

def hello():
  x = 5
print(x)
hello()
x = 5
print(f"The global variable is {x}")


x = 10  # global variable


def my_function():
  global x
  x = 5  # this will change the value of the global variable x
  y = 5  # local variable


my_function()
print(x)  # prints 5
print(y) # this will cause an error because y is a local variable and is not accessible outside of the function

x = 10
def globalvariable():
  global x
  x = 4
  print(x)

globalvariable()

# File IO in Python
# Reading a file
f = open('Myfile.txt', 'r')
text = f.read()
print(text)
f.close()

# writing a file

f = open('Myfile.txt', 'w')
f.write("I am a pyhton coder")
f.close()
#Apending

f = open('Myfile.txt', 'a')
f.write("I am a pyhton coder")
f.close()

# gorgeous type
with open('Myfile.txt', 'a') as f:
  f.write("I am a good boy")