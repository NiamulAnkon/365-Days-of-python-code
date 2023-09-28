email = input("Enter your email: ")
k, j, d = 0, 0, 0
if len(email) >= 6:
  if email[0].isalpha():
    if("@" in email) and (email.count("@") == 1):
      if (email[-4] == ".") ^ (email[-3] == "."):
        for a in email:
          if a == a.isspace():
            k = 1
          elif a.isalpha():
            if a == a.upper():
              j = 1

          elif a.isdigit():
            continue

          elif a == "_" or a == "." or a == "@":
            continue

          else:
            d = 1
          
        if k == 1 or j==1 or d==1:
          print("Wrong email condition 5")

        else:
          print("this is an Right email")

      else:
        print("Wrong email condition 4")

    else:
      print("Wrong email condition 3")

  else:
    print("Wrong email condition 2")

else:
  print("Wrond email condition 1")