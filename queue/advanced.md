Sure! Here are **10 advanced-level queue problems** along with detailed solutions and explanations in Python.

---

### 1. **Sliding Window Maximum**

**Problem:** Given an array `nums` and a window size `k`, find the maximum value in each sliding window.

**Solution:**

```python
from collections import deque

def max_sliding_window(nums, k):
    q = deque()  # will store indices of elements, largest at front
    result = []

    for i, num in enumerate(nums):
        # Remove indices out of the current window
        while q and q[0] <= i - k:
            q.popleft()

        # Remove smaller elements from the back
        while q and nums[q[-1]] < num:
            q.pop()

        q.append(i)

        # Start adding to results once the first window is ready
        if i >= k - 1:
            result.append(nums[q[0]])

    return result

# Example
print(max_sliding_window([1,3,-1,-3,5,3,6,7], 3))
# Output: [3, 3, 5, 5, 6, 7]
```

**Explanation:**
We use a deque to keep indexes of useful elements for the current window, maintaining the deque in decreasing order of values. The front of the deque is always the max element in the current window.

---

### 2. **Design a Hit Counter**

**Problem:** Design a hit counter which counts the number of hits received in the past 5 minutes.

**Solution:**

```python
from collections import deque

class HitCounter:
    def __init__(self):
        self.hits = deque()

    def hit(self, timestamp):
        self.hits.append(timestamp)

    def get_hits(self, timestamp):
        # Remove hits older than 5 minutes (300 seconds)
        while self.hits and self.hits[0] <= timestamp - 300:
            self.hits.popleft()
        return len(self.hits)

# Example
hc = HitCounter()
hc.hit(1)
hc.hit(2)
hc.hit(300)
print(hc.get_hits(300))  # 3
print(hc.get_hits(301))  # 2
```

**Explanation:**
We keep timestamps of hits in a queue, and remove any hits older than 300 seconds (5 minutes) when querying.

---

### 3. **First Unique Character in a Stream**

**Problem:** Given a stream of characters, find the first non-repeating character at any point in the stream.

**Solution:**

```python
from collections import deque, Counter

class FirstUnique:
    def __init__(self):
        self.count = Counter()
        self.queue = deque()

    def add(self, ch):
        self.count[ch] += 1
        self.queue.append(ch)
        # Remove all characters from the front that are repeated
        while self.queue and self.count[self.queue[0]] > 1:
            self.queue.popleft()

    def first_unique(self):
        return self.queue[0] if self.queue else None

# Example
fu = FirstUnique()
for ch in "aabc":
    fu.add(ch)
    print(fu.first_unique())
# Output: a, a, b, b
```

**Explanation:**
Use a queue to store order of characters and a counter to track counts. Always pop from the front until the character at front is unique.

---

### 4. **Shortest Path in Binary Matrix**

**Problem:** Given an n x n binary matrix, find the shortest path from top-left to bottom-right using 8-directional moves (0 = free cell, 1 = blocked).

**Solution:**

```python
from collections import deque

def shortest_path_binary_matrix(grid):
    n = len(grid)
    if grid[0][0] != 0 or grid[-1][-1] != 0:
        return -1

    directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
    q = deque([(0, 0, 1)])  # (row, col, distance)
    visited = {(0,0)}

    while q:
        r, c, dist = q.popleft()
        if r == c == n-1:
            return dist
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and (nr,nc) not in visited:
                visited.add((nr,nc))
                q.append((nr,nc,dist+1))
    return -1

# Example
grid = [[0,1],[1,0]]
print(shortest_path_binary_matrix(grid))  # Output: 2
```

**Explanation:**
Use BFS to find shortest path on grid with 8 directions allowed.

---

### 5. **Task Scheduler**

**Problem:** Given tasks and cooldown `n`, find least intervals to finish all tasks.

**Solution:**

```python
from collections import Counter

def least_interval(tasks, n):
    counts = Counter(tasks)
    max_freq = max(counts.values())
    max_count = sum(1 for c in counts.values() if c == max_freq)
    intervals = (max_freq - 1) * (n + 1) + max_count
    return max(intervals, len(tasks))

# Example
print(least_interval(["A","A","A","B","B","B"], 2))  # Output: 8
```

**Explanation:**
Calculate how many intervals are needed based on the most frequent tasks and the cooldown requirement.

---

### 6. **Moving Average from Data Stream**

**Problem:** Calculate moving average of last `k` elements from a stream.

**Solution:**

```python
from collections import deque

class MovingAverage:
    def __init__(self, size):
        self.size = size
        self.queue = deque()
        self.sum = 0

    def next(self, val):
        if len(self.queue) == self.size:
            self.sum -= self.queue.popleft()
        self.queue.append(val)
        self.sum += val
        return self.sum / len(self.queue)

# Example
ma = MovingAverage(3)
print(ma.next(1))  # 1.0
print(ma.next(10)) # 5.5
print(ma.next(3))  # 4.6667
print(ma.next(5))  # 6.0
```

**Explanation:**
Use a queue to hold last `k` values, track sum to get average in O(1) time.

---

### 7. **Design Circular Queue**

**Problem:** Implement a circular queue with operations: enqueue, dequeue, front, rear, isEmpty, isFull.

**Solution:**

```python
class MyCircularQueue:
    def __init__(self, k):
        self.queue = [0]*k
        self.head = -1
        self.tail = -1
        self.size = k

    def enQueue(self, value):
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = 0
        self.tail = (self.tail + 1) % self.size
        self.queue[self.tail] = value
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        if self.head == self.tail:
            self.head = self.tail = -1
        else:
            self.head = (self.head + 1) % self.size
        return True

    def Front(self):
        return -1 if self.isEmpty() else self.queue[self.head]

    def Rear(self):
        return -1 if self.isEmpty() else self.queue[self.tail]

    def isEmpty(self):
        return self.head == -1

    def isFull(self):
        return (self.tail + 1) % self.size == self.head

# Example
cq = MyCircularQueue(3)
print(cq.enQueue(1))  # True
print(cq.enQueue(2))  # True
print(cq.enQueue(3))  # True
print(cq.enQueue(4))  # False
print(cq.Rear())      # 3
print(cq.isFull())    # True
print(cq.deQueue())   # True
print(cq.enQueue(4))  # True
print(cq.Rear())      # 4
```

**Explanation:**
We simulate a circular array using modulo arithmetic.

---

### 8. **Task Scheduler with Variable Cooldown**

**Problem:** Given tasks and a cooldown time for each task type, find the minimum time to finish all tasks.

**Solution Outline:**
This is a complex extension of Task Scheduler and often solved using priority queues and a waiting queue with timestamps to track cooldown.

Due to complexity, here’s a **brief** approach:

* Use a max heap for tasks sorted by count.
* Use a queue to track tasks in cooldown with their cooldown expiration time.
* At each time unit:

  * If heap not empty, pop and execute task.
  * Put task in cooldown queue if it needs to wait.
  * When cooldown expires, push task back into heap.
* Continue until all tasks processed.

---

### 9. **Shortest Distance to a Character**

**Problem:** Given a string `S` and a character `C`, return an array of distances to the closest occurrence of `C` for each character.

**Solution:**

```python
def shortest_to_char(S, C):
    n = len(S)
    result = [float('inf')] * n

    # Forward pass
    prev = -float('inf')
    for i in range(n):
        if S[i] == C:
            prev = i
        result[i] = i - prev

    # Backward pass
    prev = float('inf')
    for i in range(n-1, -1, -1):
        if S[i] == C:
            prev = i
        result[i] = min(result[i], prev - i)

    return result

# Example
print(shortest_to_char("loveleetcode", "e"))
# Output: [3,2,1,0,1,0,0,1,2,2,1,0]
```

**Explanation:**
We do two passes to find closest occurrence from left and right.

---

### 10. **Sliding Window Median**

**Problem:** Given an array and window size k, find median of every window.

**Solution Outline:**
This problem requires two heaps (max heap and min heap) to maintain the window elements. We balance heaps to find median efficiently.

---

If you want, I can provide full code for the more complex ones like **Task Scheduler with variable cooldown** or **Sliding Window Median** — just ask! Would you like me to continue?
