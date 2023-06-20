import time
def gs():
    t = time.strftime('%H:%M:%S') 
    hour1 = int(time.strftime('%H'))
    hour = int(input("Enter hour: "))
    name = input("Enter Your Name: ")
    if(hour>=0 and hour<12):
        print("It's", hour , "O'clock Good Morning Sir" , name)
    elif(hour>=12 and hour<=5):
     print("It's", hour, "O'clock Good Afternoon Sir" , name)
    elif(hour>=6 and hour <=8):
        print("It's",hour, "O'clock Good Eveing Sir" , name)
    elif(hour>=9 and hour<=0):
        print("It's", hour, "O'clock Good Night Sir" , name)
gs()