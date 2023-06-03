#Finally Keyword
def func():
  try:
    l = [1,2,3,4]
    i = int(input("Enter the Index: "))
    print(l[i])
  except:
    print("Something went wrong")
  
  finally:
    print("I am ok")
func()
#Without Function
try:
   l = [1,2,3,4]
   i = int(input("Enter the Index: "))
   print(l[i])
except:
   print("Something went wrong")
  
finally:
  print("I am ok")