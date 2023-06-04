#Enumerate Function
marks = [12, 56, 32, 100, 12,  45, 1, 4]
# Without Enmurate function
index = 0
for mark in marks:
  print(mark)
  if(index == 3):
    print("Ankon is the best student in the world\n this is without Enumerate function")
  index +=1

# With Emunarate function
for index, mark in enumerate(marks, start=1):
  print(mark)
  if(index == 3):
    print("Ankonis the best student in the world\n this is with Enumerate function")