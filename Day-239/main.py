# Design a food ordering system where your python program will run two threads,
# Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
# Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.


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

if __name__ == "__main__":
    orders = ['pizza','samosa','pasta','biryani','burger']


    t1 = threading.Thread(target=Place_Order, args=(orders,))
    t2 = threading.Thread(target=ServeOrder)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
