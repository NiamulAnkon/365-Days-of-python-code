# OS MODULE
import os

if(not os.path.exists("data")):
    os.mkdir("data")

for i in range(0, 100):
    os.mkdir(f"data/Day{i+1}")

folders = os.listdir("data")

print(os.getcwd())
os.chdir("/Users")
print(os.getcwd())

for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))



for i in range(0, 100):
    os.rename(f"data/Tutorial{i+1}", f"data/Tutorial {i+1}")

print(os.getcwd())