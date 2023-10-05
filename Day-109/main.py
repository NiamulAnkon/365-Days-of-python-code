from time import *
import random as r


def mistake(partest, usrtest):
  error = 0
  for i in range(len(partest)):
    try:
      if partest[i] != usrtest:
        error = error + 1
    except:
      error = error + 1

  return error


def speed_time(time_s, time_e, usrinput):
  time_delay = time_e - time_s
  time_round = round(time_delay, 2)
  speed = len(usrinput) / time_round
  return round(speed)


test = [
    "a qucik brown fox jumps over the lazy dog", "i am writing",
    "what is this typing", "hello"
    ]
test_1 = r.choice(test)
print("   ** Typing Speed Calculator **")
print(test_1)
print()
print()
time_1 = time()
test_input = input("Enetr")
time_2 = time()

print(f'Speed : {speed_time(time_1, time_2, test_input)} w/sec')
print(f"error : {mistake(test_1, test_input)}")
