
import random

id_s = ["1065","8252","2193","2742","1789",
        "2335","2273","2198","2335","2273",
        "2198","2335","2273","2198","2335"]

usr_name = input("Enter your name: ")
usr_id = random.choice(id_s)
print(f"Your name is: {usr_name} \nYour id is: {usr_id}")

while True:
  make_sure = input("Are you ready to go y/n: ")
  if make_sure == "y":
    print("ok your ready to go")
  else:
    break
  
  qus_1 = ["a)What is the capital of france"]
  option_ans = ["a)Paris", "b)London", "c)Berlin", "d)Madrid"]
  print(qus_1)
  print(option_ans)
  option = ["a","b","c","d"]
  ans = input("Enter your ans a,b,c,d: ")
  if ans == option[0]:
    print("Congrats your ans is correct")
  else:
    print(f"Sorry your ans is wrong the correct ans is {option[0]}")
  
  qus_2 = ["a)What is the capital of german"]
  option_ans = ["a)Paris", "b)London", "c)Berlin", "d)Madrid"]
  print(qus_2)
  print(option_ans)
  option = ["a","b","c","d"]
  ans = input("Enter your ans a,b,c,d: ")
  if ans == option[2]:
    print("Congrats your ans is correct")
  else:
    print(f"Sorry your ans is wrong the correct ans is {option[2]}")
  
  qus_3 = ["a)What is the capital of Bangladesh"]
  option_ans = ["a)Paris", "b)London", "c)Berlin", "d)Dhaka"]
  print(qus_3)
  print(option_ans)
  option = ["a","b","c","d"]
  ans = input("Enter your ans a,b,c,d: ")
  if ans == option[3]:
    print("Congrats your ans is correct")
  else:
    print(f"Sorry your ans is wrong the correct ans is {option[3]}")

  retry = input("Do you want to try again y/n: ")
  if retry == "y":
    continue
  else:
    break