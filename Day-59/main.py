#Exercise Clear the Clutter
import os 
i = 1
files = os.listdir("clutter")

for file in files:
  if file.endswith(".png"):
    print(file)
  else:
    print("something went wrong")
  os.rename(f"clutter/{file}", f"{i}.png")
  i = i + 1