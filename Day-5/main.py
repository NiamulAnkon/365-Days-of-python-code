def avarage(a, b):
    print("the avarage is ", (a+b)/2)

avarage(4,6)
# define values under the function variables
def avarage(a=9, b=5):
    print("The avarage is ", (a+b)/2)

avarage()
# replace the values of a and b when calling it
def avarage(a=9, b=5):
    print("The avarage is ", (a+b)/2)

avarage(1, 5)
# only change the a value when calling it
def avarage(a=9, b=5):
    print("The avarage is ", (a+b)/2)

avarage(1)
# change the b value when calling it
def avarage(a=9, b=5):
    print("The avarage is ", (a+b)/2)

avarage(b =  5)

def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)

name("Niamul","Islam","Ankon")

def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")

#list
l = [8,9,8,7,0,5,1,2,3,4,5,6]
print(l)
print(l)
l.append(7)
l.sort()
l.reverse()
print(l.index(2))
print(l.count(8))
m = l.copy()
m[0] = 0
print(l)
l.insert(1, 899)
m = [900,1000,1100]
k = l + m
l.extend(m)
print(k)

#tuples
tup = (1,5,6,342, 654, "Ankon", True)
print(type(tup), tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])

if 342 in tup:
  print("bra")
else:
  print("arb")

tup2 = tup[1:4]
print(tup2)

#Tuples Operations
tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
res = tuple1.count(3)
res = tuple1.index(3)
res = tuple1.index(3, 4, 8)
res = len(tuple1)
print('Count of 3 in tuple1 is:', res)
def avarage(a, b):
    print("the avarage is ", (a+b)/2)

avarage(4,6)
# define values under the function variables
def avarage(a=9, b=5):
    print("The avarage is ", (a+b)/2)

avarage()
# replace the values of a and b when calling it
def avarage(a=9, b=5):
    print("The avarage is ", (a+b)/2)

avarage(1, 5)
# only change the a value when calling it
def avarage(a=9, b=5):
    print("The avarage is ", (a+b)/2)

avarage(1)
# change the b value when calling it
def avarage(a=9, b=5):
    print("The avarage is ", (a+b)/2)

avarage(b =  5)

def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)

name("Niamul","Islam","Ankon")

def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")

#list
l = [8,9,8,7,0,5,1,2,3,4,5,6]
print(l)
print(l)
l.append(7)
l.sort()
l.reverse()
print(l.index(2))
print(l.count(8))
m = l.copy()
m[0] = 0
print(l)
l.insert(1, 899)
m = [900,1000,1100]
k = l + m
l.extend(m)
print(k)

#tuples
tup = (1,5,6,342, 654, "Ankon", True)
print(type(tup), tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])

if 342 in tup:
  print("bra")
else:
  print("arb")

tup2 = tup[1:4]
print(tup2)

#Tuples Operations
tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
res = tuple1.count(3)
res = tuple1.index(3)
res = tuple1.index(3, 4, 8)
res = len(tuple1)
print('Count of 3 in tuple1 is:', res)
