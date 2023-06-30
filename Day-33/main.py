import random as r
try:
  def Ticketbuy():
    name = input("Enter the name for your ticket: ")
    date = int(input("Enter the date of you ticket for your bus \n type the date only: "))
    time = input("Enter the time day/night: ")
    # t_opt = ["day", "night"]
    sit = ["a1","a2","b1","b2","b3","b4","c1","c2"]
    take_sit = r.choice(sit)
    print(f"Your name is {name}\n Your Date is {date}\n Your time is {time}\n Your sit is {take_sit}")
except:
  print("Something went wrong please try again")

Ticketbuy()