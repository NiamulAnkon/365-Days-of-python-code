#MultiProcessing
import multiprocessing 
import requests
import concurrent.futures

def donwloadfile(url, name):
  print(f"start download {name}")
  response = requests.get(url)
  open(f"files/file {name}.jpg", "wb").write(response.content)
  print(f"Finished Downloading {name}")

url = "https://picsum.photos/2000/3000"
pros = []

for i in range(5):
  # donwloadfile(url, i)
  p = multiprocessing.Process(target=donwloadfile, args=[url, i])
  p.start()
  pros.append(p)

for p in pros:
  p.join()

with concurrent.futures.ProcessPoolExecutor() as executor:
  li1 = [url for i in range(60)]
  li2 = [i for i in range(60)]
  results = executor.map(donwloadfile, li1, li2)
  for a in results:
    print(a)