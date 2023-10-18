import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time

# Specify the folder path where you want to save the video
output_folder = "D:/ankonFolder/365daysofcode/Day-122"
output_filename = "output.avi"
output_path = output_folder + output_filename

width = GetSystemMetrics(0)
heigth = GetSystemMetrics(1)

dim = (width, heigth)

f = cv2.VideoWriter_fourcc(*'XVID')

# Use the full path to the output video file
output = cv2.VideoWriter(output_path, f, 30.0, dim)

now_time = time.time()
dur = 10

end_time = now_time + dur
while True:
    img = pyautogui.screenshot()
    frame_1 = np.array(img)
    frame = cv2.cvtColor(frame_1, cv2.COLOR_BGR2RGB)
    output.write(frame)
    c_time = time.time()
    if c_time > end_time:
        break
    time.sleep(0.1)
output.release()

print("Video saved to:", output_path)
print("----END----")
