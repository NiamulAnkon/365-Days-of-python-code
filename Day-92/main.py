#Function Caching
import functools
import time

@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5

print(fx(20))
print("Done for 20")
print(fx(40))
print("Done for 40")
print(fx(60))
print("Done for 60")

print(fx(20))
print("Done for 20")
print(fx(40))
print("Done for 40")
print(fx(60))
print("Done for 60")

print(fx(5))
print("Done for 5")