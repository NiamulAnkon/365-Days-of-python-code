#100 file download
import multiprocessing 
import requests

def donwloadfile(url, name):
  print(f"start download {name}")
  response = requests.get(url)
  open(f"files/file {name}.jpg", "wb").write(response.content)
  print(f"Finished Downloading {name}")

url = "https://picsum.photos/2000/3000"
pros = []

for i in range(100):
  donwloadfile(url, i)
  p = multiprocessing.Process(target=donwloadfile, args=[url, i])
  p.start()
  pros.append(p)

for p in pros:
  p.join()