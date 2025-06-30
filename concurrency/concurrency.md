Sure! Here are **10 concurrency problems** with solutions and detailed explanations. These problems are common in programming related to multi-threading, synchronization, and parallel execution.

---

## 1. **Print numbers from 1 to N using two threads alternatively**

**Problem:**
Two threads print numbers from 1 to N alternatively, i.e., thread A prints odd numbers and thread B prints even numbers.

### Solution:

```python
import threading

class AlternatePrinter:
    def __init__(self, n):
        self.n = n
        self.num = 1
        self.lock = threading.Lock()
        self.turn = 1  # 1 for odd thread, 0 for even thread

    def print_odd(self):
        while self.num <= self.n:
            with self.lock:
                if self.turn == 1 and self.num % 2 == 1:
                    print(f"Odd Thread: {self.num}")
                    self.num += 1
                    self.turn = 0

    def print_even(self):
        while self.num <= self.n:
            with self.lock:
                if self.turn == 0 and self.num % 2 == 0:
                    print(f"Even Thread: {self.num}")
                    self.num += 1
                    self.turn = 1

n = 10
printer = AlternatePrinter(n)
t1 = threading.Thread(target=printer.print_odd)
t2 = threading.Thread(target=printer.print_even)

t1.start()
t2.start()

t1.join()
t2.join()
```

**Explanation:**
Two threads share a lock and a shared counter. The `turn` variable controls which thread can print. Only the thread whose turn matches prints the number and then switches the turn.

---

## 2. **Producer-Consumer Problem using Semaphore**

**Problem:**
Implement producer-consumer synchronization where producers add items to a buffer and consumers remove items, ensuring no race conditions.

### Solution:

```python
import threading
import time
import random

class ProducerConsumer:
    def __init__(self):
        self.buffer = []
        self.capacity = 5
        self.lock = threading.Lock()
        self.empty = threading.Semaphore(self.capacity)  # Slots available
        self.full = threading.Semaphore(0)               # Items available

    def producer(self):
        while True:
            item = random.randint(1, 100)
            self.empty.acquire()  # Wait if buffer is full
            with self.lock:
                self.buffer.append(item)
                print(f"Produced: {item}")
            self.full.release()  # Signal item available
            time.sleep(random.random())

    def consumer(self):
        while True:
            self.full.acquire()  # Wait if buffer empty
            with self.lock:
                item = self.buffer.pop(0)
                print(f"Consumed: {item}")
            self.empty.release()  # Signal slot available
            time.sleep(random.random())

pc = ProducerConsumer()
t1 = threading.Thread(target=pc.producer)
t2 = threading.Thread(target=pc.consumer)

t1.start()
t2.start()
```

**Explanation:**
We use two semaphores: `empty` (number of free slots) and `full` (number of filled slots). Producer waits if buffer is full (`empty == 0`), consumer waits if buffer empty (`full == 0`). Lock protects the shared buffer.

---

## 3. **Dining Philosophers Problem**

**Problem:**
Five philosophers sit at a round table with five forks. Each needs two forks to eat. Implement a solution preventing deadlock.

### Solution:

```python
import threading
import time

class Philosopher(threading.Thread):
    def __init__(self, left_fork, right_fork, id):
        threading.Thread.__init__(self)
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.id = id

    def run(self):
        for _ in range(5):
            print(f"Philosopher {self.id} is thinking.")
            time.sleep(1)
            print(f"Philosopher {self.id} is hungry.")
            self.dine()

    def dine(self):
        # Prevent deadlock by odd philosopher picking left first, even picking right first
        first_fork, second_fork = (self.left_fork, self.right_fork) if self.id % 2 == 0 else (self.right_fork, self.left_fork)

        with first_fork:
            print(f"Philosopher {self.id} picked up first fork.")
            with second_fork:
                print(f"Philosopher {self.id} picked up second fork and is eating.")
                time.sleep(2)
            print(f"Philosopher {self.id} put down second fork.")
        print(f"Philosopher {self.id} put down first fork.")

forks = [threading.Lock() for _ in range(5)]
philosophers = [Philosopher(forks[i], forks[(i+1) % 5], i) for i in range(5)]

for p in philosophers:
    p.start()
for p in philosophers:
    p.join()
```

**Explanation:**
To avoid deadlock, we alternate the order in which philosophers pick up forks based on their ID parity. Odd philosophers pick right fork first, even pick left fork first.

---

## 4. **Thread-safe Singleton Pattern**

**Problem:**
Implement a singleton pattern in Python ensuring thread safety.

### Solution:

```python
import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()

print(s1 is s2)  # True
```

**Explanation:**
Double-checked locking ensures only one instance is created even with multiple threads accessing the class simultaneously.

---

## 5. **Read-Write Lock**

**Problem:**
Implement a read-write lock that allows multiple readers but only one writer at a time.

### Solution:

```python
import threading

class ReadWriteLock:
    def __init__(self):
        self.readers = 0
        self.lock = threading.Lock()
        self.write_lock = threading.Lock()

    def acquire_read(self):
        with self.lock:
            self.readers += 1
            if self.readers == 1:
                self.write_lock.acquire()

    def release_read(self):
        with self.lock:
            self.readers -= 1
            if self.readers == 0:
                self.write_lock.release()

    def acquire_write(self):
        self.write_lock.acquire()

    def release_write(self):
        self.write_lock.release()

rw_lock = ReadWriteLock()

def reader():
    rw_lock.acquire_read()
    print("Reading")
    rw_lock.release_read()

def writer():
    rw_lock.acquire_write()
    print("Writing")
    rw_lock.release_write()

# Usage with threads omitted for brevity
```

**Explanation:**
Multiple readers can enter concurrently; the first reader acquires the write lock, blocking writers. Writers acquire the write lock exclusively.

---

## 6. **Barrier Synchronization**

**Problem:**
Implement a barrier so that multiple threads wait for each other at a synchronization point.

### Solution:

```python
import threading
import time

class Barrier:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.lock = threading.Lock()
        self.turnstile = threading.Event()

    def wait(self):
        with self.lock:
            self.count += 1
            if self.count == self.n:
                self.turnstile.set()
        self.turnstile.wait()

def worker(barrier, id):
    print(f"Thread {id} before barrier")
    barrier.wait()
    print(f"Thread {id} after barrier")

barrier = Barrier(3)
threads = [threading.Thread(target=worker, args=(barrier, i)) for i in range(3)]

for t in threads: t.start()
for t in threads: t.join()
```

**Explanation:**
Each thread increments a counter, and the last thread sets an event allowing all to proceed. Threads wait on the event before continuing.

---

## 7. **Deadlock Detection**

**Problem:**
Given a scenario with threads and locks, detect if deadlock is possible.

### Explanation and Solution Approach:

This is a complex problem that involves building a **Resource Allocation Graph (RAG)** and checking for cycles.

* **Approach:**
  Represent threads and locks as nodes.
* An edge from thread to lock means the thread is waiting for the lock.
* An edge from lock to thread means the lock is held by the thread.
  Deadlock if the graph has cycles.

### Simple example for cycle detection:

```python
from collections import defaultdict

class DeadlockDetector:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def is_cyclic_util(self, v, visited, rec_stack):
        visited[v] = True
        rec_stack[v] = True
        for neighbour in self.graph[v]:
            if not visited[neighbour]:
                if self.is_cyclic_util(neighbour, visited, rec_stack):
                    return True
            elif rec_stack[neighbour]:
                return True
        rec_stack[v] = False
        return False

    def detect_deadlock(self):
        visited = {node: False for node in self.graph}
        rec_stack = {node: False for node in self.graph}
        for node in self.graph:
            if not visited[node]:
                if self.is_cyclic_util(node, visited, rec_stack):
                    return True
        return False

dd = DeadlockDetector()
dd.add_edge('Thread1', 'Lock1')
dd.add_edge('Lock1', 'Thread2')
dd.add_edge('Thread2', 'Lock2')
dd.add_edge('Lock2', 'Thread1')  # Cycle -> deadlock

print(dd.detect_deadlock())  # True
```

---

## 8. **Atomic Counter**

**Problem:**
Implement a thread-safe atomic counter.

### Solution:

```python
import threading

class AtomicCounter:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def increment(self):
        with self._lock:
            self.value += 1
            return self.value

counter = AtomicCounter()

def worker():
    for _ in range(1000):
        counter.increment()

threads = [threading.Thread(target=worker) for _ in range(10)]

for t in threads: t.start()
for t in threads: t.join()

print(counter.value)  # Should be 10000
```

**Explanation:**
Lock ensures increments are atomic and thread-safe.

---

## 9. **Implement Thread Pool**

**Problem:**
Implement a basic thread pool that executes submitted tasks using a fixed number of threads.

### Solution:

```python
import threading
from queue import Queue

class ThreadPool:
    def __init__(self, num_threads):
        self.tasks = Queue()
        self.workers = []
        self.num_threads = num_threads
        self.is_running = True

        for _ in range(num_threads):
            t = threading.Thread(target=self.worker)
            t.start()
            self.workers.append(t)

    def worker(self):
        while self.is_running:
            try:
                func, args = self.tasks.get(timeout=1)
                func(*args)
                self.tasks.task_done()
            except:
                pass

    def submit(self, func, *args):
        self.tasks.put((func, args))

    def shutdown(self):
        self.is_running = False
        for w in self.workers:
            w.join()

def print_task(name):
    print(f"Hello from {name}")

pool = ThreadPool(3)
for i in range(10):
    pool.submit(print_task, f"Task-{i}")

pool.tasks.join()
pool.shutdown()
```

**Explanation:**
Tasks are put into a queue, and worker threads pick and execute them concurrently.

---

## 10. **Implement Countdown Latch**

**Problem:**
Implement a countdown latch that blocks until a set number of events have occurred.

### Solution:

```python
import threading

class CountDownLatch:
    def __init__(self, count):
        self.count = count
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)

    def count_down(self):
        with self.lock:
            self.count -= 1
            if self.count == 0:
                self.condition.notify_all()

    def wait(self):
        with self.lock:
            while self.count > 0:
                self.condition.wait()

latch = CountDownLatch(3)

def worker(id):
    print(f"Worker {id} started")
    # Simulate work
    import time
    time.sleep(id)
    print(f"Worker {id} finished")
    latch.count_down()

for i in range(3):
    threading.Thread(target=worker, args=(i+1,)).start()

print("Main thread waiting for workers")
latch.wait()
print("All workers finished")
```

**Explanation:**
The main thread waits on the latch until the count reaches zero via `count_down()` calls by workers.

---

If you want me to provide concurrency problems of a particular type or deeper explanations/examples, just let me know!
