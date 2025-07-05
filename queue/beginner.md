Sure! Here are **10 beginner-level queue problems** with solutions and detailed explanations in Python:

---

### 1. **Implement a Queue using List**

**Problem:** Implement a queue with enqueue, dequeue, and peek operations using a Python list.

**Solution:**

```python
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        return None

    def peek(self):
        if self.queue:
            return self.queue[0]
        return None

# Example
q = Queue()
q.enqueue(10)
q.enqueue(20)
print(q.peek())    # Output: 10
print(q.dequeue()) # Output: 10
print(q.peek())    # Output: 20
```

**Explanation:**
We use a list where appending at the end simulates enqueue, and popping from the front simulates dequeue. The peek returns the first element.

---

### 2. **Check if a Queue is Palindrome**

**Problem:** Given a queue, check if its elements form a palindrome.

**Solution:**

```python
from collections import deque

def is_palindrome(queue):
    arr = list(queue)
    return arr == arr[::-1]

# Example
q = deque([1, 2, 3, 2, 1])
print(is_palindrome(q))  # Output: True
```

**Explanation:**
Convert the queue to a list and check if it reads the same forward and backward.

---

### 3. **Reverse a Queue**

**Problem:** Reverse the elements of a queue.

**Solution:**

```python
from collections import deque

def reverse_queue(q):
    stack = []
    while q:
        stack.append(q.popleft())
    while stack:
        q.append(stack.pop())

# Example
q = deque([1, 2, 3, 4])
reverse_queue(q)
print(list(q))  # Output: [4, 3, 2, 1]
```

**Explanation:**
Use a stack to reverse order: dequeue all elements into a stack, then enqueue back.

---

### 4. **Implement a Circular Queue**

**Problem:** Implement a fixed-size circular queue.

**Solution:**

```python
class CircularQueue:
    def __init__(self, k):
        self.queue = [None]*k
        self.head = self.tail = -1
        self.size = k

    def enqueue(self, val):
        if (self.tail + 1) % self.size == self.head:
            return False  # Queue is full
        if self.head == -1:
            self.head = 0
        self.tail = (self.tail + 1) % self.size
        self.queue[self.tail] = val
        return True

    def dequeue(self):
        if self.head == -1:
            return None  # Queue is empty
        val = self.queue[self.head]
        if self.head == self.tail:
            self.head = self.tail = -1
        else:
            self.head = (self.head + 1) % self.size
        return val

# Example
cq = CircularQueue(3)
print(cq.enqueue(1))  # True
print(cq.enqueue(2))  # True
print(cq.enqueue(3))  # True
print(cq.enqueue(4))  # False (full)
print(cq.dequeue())   # 1
print(cq.enqueue(4))  # True
```

**Explanation:**
Use a fixed-size list and two pointers `head` and `tail`. Wrap around when reaching the end.

---

### 5. **Find First Non-Repeating Character in a Stream**

**Problem:** Given a stream of characters, find the first non-repeating character at each insertion.

**Solution:**

```python
from collections import deque, Counter

def first_non_repeating(stream):
    q = deque()
    count = Counter()
    result = []

    for ch in stream:
        count[ch] += 1
        q.append(ch)
        while q and count[q[0]] > 1:
            q.popleft()
        if q:
            result.append(q[0])
        else:
            result.append('#')
    return result

# Example
stream = "aabc"
print(first_non_repeating(stream))  # Output: ['a', '#', 'b', 'b']
```

**Explanation:**
Use a queue to track characters and a counter to check repetition. Remove repeating chars from front.

---

### 6. **Implement Stack using Two Queues**

**Problem:** Implement a stack using two queues.

**Solution:**

```python
from collections import deque

class StackUsingQueues:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        return self.q1.popleft() if self.q1 else None

    def top(self):
        return self.q1[0] if self.q1 else None

# Example
s = StackUsingQueues()
s.push(10)
s.push(20)
print(s.top())  # Output: 20
print(s.pop())  # Output: 20
print(s.pop())  # Output: 10
```

**Explanation:**
Push element to empty queue and pour existing elements after it to maintain stack order.

---

### 7. **Implement Queue using Two Stacks**

**Problem:** Implement a queue using two stacks.

**Solution:**

```python
class QueueUsingStacks:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, x):
        self.s1.append(x)

    def dequeue(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop() if self.s2 else None

# Example
q = QueueUsingStacks()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # Output: 1
print(q.dequeue())  # Output: 2
```

**Explanation:**
Use s1 to enqueue and s2 to dequeue, transferring elements only when s2 is empty.

---

### 8. **Generate Binary Numbers from 1 to N**

**Problem:** Generate binary representations of numbers from 1 to N using a queue.

**Solution:**

```python
from collections import deque

def generate_binary(n):
    result = []
    q = deque()
    q.append("1")

    for _ in range(n):
        front = q.popleft()
        result.append(front)
        q.append(front + "0")
        q.append(front + "1")

    return result

# Example
print(generate_binary(5))  # Output: ['1', '10', '11', '100', '101']
```

**Explanation:**
Use BFS on binary numbers by appending "0" and "1" at each step.

---

### 9. **Sliding Window Maximum**

**Problem:** Find the maximum in each sliding window of size k in an array.

**Solution:**

```python
from collections import deque

def max_sliding_window(nums, k):
    q = deque()  # Store indices
    result = []

    for i, num in enumerate(nums):
        while q and nums[q[-1]] <= num:
            q.pop()
        q.append(i)
        if q[0] == i - k:
            q.popleft()
        if i >= k - 1:
            result.append(nums[q[0]])
    return result

# Example
nums = [1,3,-1,-3,5,3,6,7]
print(max_sliding_window(nums, 3))  # Output: [3,3,5,5,6,7]
```

**Explanation:**
Maintain indices of useful elements in deque to get max in O(1) per window.

---

### 10. **Rotting Oranges**

**Problem:** Given a grid of oranges, every minute, rotten oranges infect adjacent fresh oranges. Find time until no fresh oranges remain.

**Solution:**

```python
from collections import deque

def orangesRotting(grid):
    rows, cols = len(grid), len(grid[0])
    q = deque()
    fresh = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                q.append((r,c))
            elif grid[r][c] == 1:
                fresh += 1

    time = 0
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while q and fresh > 0:
        for _ in range(len(q)):
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr,nc))
        time += 1

    return time if fresh == 0 else -1

# Example
grid = [
    [2,1,1],
    [1,1,0],
    [0,1,1]
]
print(orangesRotting(grid))  # Output: 4
```

**Explanation:**
Use BFS starting from rotten oranges to infect adjacent fresh oranges each minute.

---

If you want me to provide more queue problems or solutions for other data structures, just ask!
