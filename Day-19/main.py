#read(), readlines() and other methods

f = open('Myfile.txt', 'r')
i = 0
while True:
  i = i + 1
  line = f.readline()
  if not line:
    break
    print(line)
  m1 = int(line.split(",")[0])
  m2 = int(line.split(",")[1])
  m3 = int(line.split(",")[2])
  print(f"Marks of student of 1 in math: {m1*2}")
  print(f"Marks of student of 2 in englsih: {m2*2}")
  print(f"Marks of student of 3 python: {m3*2}")
  
  print(line)