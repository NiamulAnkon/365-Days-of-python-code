#Multithreading 
import threading
import time
from concurrent.futures import ThreadPoolExecutor

def function(seconds):
  print(f"sleeping for {seconds}")
  time.sleep(seconds)

def main():
  time1 = time.perf_counter()
  # function(2)
  # function(3)
  # function(1)
  # time2 = time.perf_counter()
  # print(f"It take total of {time2 - time1} seconds")
  
  t1 = threading.Thread(target=function, args=[2])
  t2 = threading.Thread(target=function, args=[3])
  t3 = threading.Thread(target=function, args=[1])
  
  t1.start()
  t2.start()
  t3.start()
  
  t1.join()
  t2.join()
  t3.join()
  
  time2 = time.perf_counter()
  print(f"It take total of {time2 - time1} seconds")

def poolingDemo():
  with ThreadPoolExecutor() as executor:
    # future1 = executor.submit(function, 3)
    # future2 = executor.submit(function, 2)
    # future3 = executor.submit(function, 1)
    # print(future1.result())
    # print(future2.result())
    # print(future3.result())
    l = [3, 5, 1, 2]
    results = executor.map(function, l)
    for result in results:
      print(result)


poolingDemo()