#strins
name = "Ankon"
friend = "Ankon"
anotherFriend = 'Ankon'
apple = '''He said,
Hi Ankon
hey I am good
"I want to eat an apple'''

print("Hello, " + name)
# print(apple)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print(name[5]) # Throws an error
print("Lets use a for loop\n")
for character in apple:
    print(character)

#STRING SLICE
fruit = "Mango"
mangoLen = len(fruit)
print(mangoLen)
print(fruit[0:4]) # including 0 but not 4
print(fruit[1:4]) # including 1 but not 4
print(fruit[:5])
print(fruit[0:-3])
print(fruit[:len(fruit)-3])
print(fruit[-1:len(fruit) - 3])
print(fruit[-3:-1])

# Strings are immutable
a = "!!!Ankon!! !!!!!!!!! Ankon"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Ankon", "Anonto"))
print(a.split(" "))
blogHeading = "introduction tO jS"
print(blogHeading.capitalize())

str1 = "Welcome to the Console!!!"
print(len(str1))
print(len(str1.center(50)))
print(a.count("Harry"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("ishh"))
# print(str1.index("ishh"))

str1 = "WelcomeToTheConsole"
print(str1.isalnum())
str1 = "Welcome"
print(str1.isalpha())

str1 = "hello world"
print(str1.islower())

str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())
str1 = "         "       #using Spacebar
print(str1.isspace())
str2 = "  "       #using Tab
print(str2.isspace())

str1 = "World Health Organization"
print(str1.istitle())

str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "Python is a Interpreted Language"
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language"
print(str1.swapcase())

str1 = "His name is Dan. Dan is an honest man."
print(str1.title())

a = int(input("Enter your age: "))
print("your age is: ", a)

if(a>18):
  print("You can take creadit card")

elif(a == 18):
  print("you need to grow more for a creadit card")
else:
  print("You can't take creadit card")