import pywhatkit as pwk
import datetime

# Get the current time
now = datetime.datetime.now()

# Define the target time
target_hour = 20  # 8 AM
target_minute = 29

# Calculate the time difference in minutes
time_diff = (target_hour - now.hour) * 60 + (target_minute - now.minute)

# Send the message after waiting for the calculated time
if time_diff > 0:
    pwk.sendwhatmsg("+8801619-663134", "Hi ki koro :)", now.hour, now.minute + time_diff)
else:
    print("The specified time has already passed.")

