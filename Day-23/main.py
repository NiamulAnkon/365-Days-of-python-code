#'is' vs '==' in Python 
a = 4
b = 4

print(a is b)# Compaires exact location of object in memory
print(a == b)# Compaires value of object in memory

a1 = 4
b1 = "4"
print(a1 is b1)
print(a1 == b1)

a2 = [1,2,3,43]
b2 = [1,2,3,43]
print(a2 == b2)
print(a2 is b2)

a3 = None
b3 = None

print(a3 is b3) # exact location of object in memory
print(a3 is None) # exact location of object in memory
print(a3== b3) # value