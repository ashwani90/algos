import threading
import time
import random

class ProducerConsumer:
    def __init__(self):
        self.buffer = []
        self.capacity = 5
        self.lock = threading.Lock()
        self.empty = threading.Semaphore(self.capacity)
        self.full = threading.Semaphore(0)
    
    def producer(self):
        while True:
            item = random.randint(1, 100)
            self.empty.acquire()
            with self.lock:
                self.buffer.append(item)
                print(item)
            self.full.release()
            time.sleep(random.random())
    
    def consumer(self):
        while True:
            self.full.acquire()
            with self.lock:
                item = self.buffer.pop(0)
                print(f"Comsumer {item}")
            self.empty.release()
            time.sleep(random.random())

pc = ProducerConsumer()
t1 = threading.Thread(target=pc.producer)
t2 = threading.Thread(target=pc.consumer)
t1.start()
t2.start()