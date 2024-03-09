# Write a program to print binary numbers from 1 to 10 using Queue. Use Queue class implemented in main tutorial.
from collections import deque
import time
import threading

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue (self, val):
        self.buffer.appendleft(val)

    def dequeue (self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size (self):
        return len(self.buffer)
    def front(self):
        return self.buffer[-1]

main_func = Queue()


def Place_Order(orders):
    for i in orders:
        main_func.enqueue(orders)
        print("Order Placed")
        time.sleep(0.5)

def ServeOrder():
    while True:
        try:
            order = main_func.dequeue()
            print(f"now serving {order}")
            time.sleep(2)
        except  IndexError:
            print("Nothing left all served")
            break
def produce_binary_numbers(n):
    numbers_queue = Queue()
    numbers_queue.enqueue("1")

    for i in range(n):
        front = numbers_queue.front()
        print("   ", front)
        numbers_queue.enqueue(front + "0")
        numbers_queue.enqueue(front + "1")

        numbers_queue.dequeue()


if __name__ == '__main__':
    produce_binary_numbers(10)