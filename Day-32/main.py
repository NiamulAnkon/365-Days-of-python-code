#I can't make snake water gun for some reason
import random as r
try:
    def snakewatergun():
      output = ["It's a Draw", "You Won", "You Lose"]
      opt = ["snake", "water", "gun"]
      p_choice = input("Chose snake, water, gun: ")
      c_choice = r.choice(opt)
      
      if(p_choice == opt[0] and c_choice == opt[1]):
        print(f"You Chose {p_choice} \n Computer Chose {c_choice} \n {output[1]}")
      elif(p_choice == opt[1] and c_choice == opt[0]):
        print(f"You Chose {p_choice} \n Computer Chose {c_choice} \n {output[2]}")
      elif(p_choice == opt[1] and c_choice == opt[2]):
        print(f"You Chose {p_choice} \n Computer Chose {c_choice} \n {output[1]}")
      elif(p_choice == opt[2] and c_choice == opt[1]):
        print(f"You Chose {p_choice} \n Computer Chose {c_choice} \n {output[2]}")
      elif(p_choice == opt[2] and c_choice == opt[0]):
        print(f"You Chose {p_choice} \n Computer Chose {c_choice} \n {output[2]}")
      elif(p_choice == opt[0] and c_choice == opt[2]):
        print(f"You Chose {p_choice} \n Computer Chose {c_choice} \n {output[2]}")
      elif(p_choice == opt[0] and c_choice == opt[0]):
        print(f"You Chose {p_choice} \n Computer Chose {c_choice} \n {output[0]}")
      elif(p_choice == opt[1] and c_choice == opt[1]):
        print(f"You Chose {p_choice} \n Computer Chose {c_choice} \n {output[0]}")
      elif(p_choice == opt[2] and c_choice == opt[2]):
        print(f"You Chose {p_choice} \n Computer Chose {c_choice} \n {output[0]}")
      else:
        print("Something went wrong")
except ValueError:
  print("Something went wrong")

snakewatergun()