Certainly! Here are **10 intermediate level queue problems** along with their solutions and detailed explanations in Python:

---

### 1. **Sliding Window Minimum**

**Problem:** Given an array and a window size `k`, find the minimum in each sliding window.

**Solution:**

```python
from collections import deque

def min_sliding_window(nums, k):
    q = deque()  # Store indices of candidates for min
    result = []

    for i, num in enumerate(nums):
        # Remove elements out of this window
        while q and q[0] <= i - k:
            q.popleft()
        # Remove elements larger than current because they won't be min
        while q and nums[q[-1]] >= num:
            q.pop()
        q.append(i)
        if i >= k - 1:
            result.append(nums[q[0]])
    return result

# Example
nums = [4,2,12,3,5,1,7]
print(min_sliding_window(nums, 3))  # Output: [2, 2, 3, 1, 1, 1]
```

**Explanation:**
Similar to the sliding window max problem, maintain a deque with indices of potentially minimal elements, removing elements that are out of the current window or not useful.

---

### 2. **First Negative Integer in Every Window of Size K**

**Problem:** Given an array, for every contiguous subarray of size `k`, find the first negative integer.

**Solution:**

```python
from collections import deque

def first_negative_in_window(nums, k):
    q = deque()
    result = []

    for i, num in enumerate(nums):
        if num < 0:
            q.append(i)
        # Remove out of window elements
        if q and q[0] <= i - k:
            q.popleft()
        if i >= k - 1:
            if q:
                result.append(nums[q[0]])
            else:
                result.append(0)
    return result

# Example
nums = [12, -1, -7, 8, 15, 30, 16, 28]
print(first_negative_in_window(nums, 3))  # Output: [-1, -1, -7, 0, 0, 0]
```

**Explanation:**
Use a deque to store indices of negative elements in the current window. The front of the deque is the first negative integer.

---

### 3. **Design a Hit Counter**

**Problem:** Design a hit counter which counts the number of hits received in the past 5 minutes (300 seconds).

**Solution:**

```python
from collections import deque
import time

class HitCounter:
    def __init__(self):
        self.hits = deque()

    def hit(self, timestamp):
        self.hits.append(timestamp)

    def get_hits(self, timestamp):
        # Remove hits older than 5 minutes
        while self.hits and self.hits[0] <= timestamp - 300:
            self.hits.popleft()
        return len(self.hits)

# Example
hc = HitCounter()
hc.hit(1)
hc.hit(2)
hc.hit(300)
print(hc.get_hits(300))  # Output: 3
print(hc.get_hits(301))  # Output: 2
```

**Explanation:**
Maintain timestamps of hits in a queue and remove those older than 300 seconds when queried.

---

### 4. **Circular Tour / Gas Station**

**Problem:** Given two arrays `gas` and `cost`, find the starting gas station index from where the vehicle can complete the circle without running out of gas.

**Solution:**

```python
def can_complete_circuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    total, start, tank = 0, 0, 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:
            start = i + 1
            tank = 0
    return start

# Example
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(can_complete_circuit(gas, cost))  # Output: 3
```

**Explanation:**
If total gas < total cost, no solution. Otherwise, the start index resets when tank < 0.

---

### 5. **Task Scheduler**

**Problem:** Given a list of tasks (represented by characters) and a cooldown interval `n`, schedule tasks such that the same task appears at least `n` intervals apart. Return the minimum time units needed.

**Solution:**

```python
from collections import Counter
import heapq

def least_interval(tasks, n):
    freq = Counter(tasks)
    max_heap = [-cnt for cnt in freq.values()]
    heapq.heapify(max_heap)
    time = 0

    while max_heap:
        temp = []
        k = n + 1
        while k > 0 and max_heap:
            cnt = heapq.heappop(max_heap)
            if cnt + 1 < 0:
                temp.append(cnt + 1)
            time += 1
            k -= 1
        for item in temp:
            heapq.heappush(max_heap, item)
        if max_heap:
            time += k  # idle time
    return time

# Example
tasks = ["A","A","A","B","B","B"]
n = 2
print(least_interval(tasks, n))  # Output: 8
```

**Explanation:**
Use a max heap to always schedule the most frequent tasks first, track cooldown using `k`.

---

### 6. **Sliding Window Median**

**Problem:** Find median of every sliding window of size `k` in the array.

**Solution:**

*Note: Intermediate version uses two heaps (min heap and max heap). Here's a simplified version using `bisect` for educational purposes.*

```python
import bisect

def sliding_window_median(nums, k):
    window = sorted(nums[:k])
    medians = []

    for i in range(k, len(nums)+1):
        # median calculation
        if k % 2 == 0:
            median = (window[k//2 - 1] + window[k//2]) / 2
        else:
            median = window[k//2]
        medians.append(median)

        if i == len(nums):
            break
        # remove nums[i-k]
        window.pop(bisect.bisect_left(window, nums[i-k]))
        # insert nums[i]
        bisect.insort_left(window, nums[i])
    return medians

# Example
nums = [1,3,-1,-3,5,3,6,7]
print(sliding_window_median(nums, 3))
# Output: [1, -1, -1, 3, 5, 6]
```

**Explanation:**
Maintain a sorted window and update it by removing the old element and inserting the new one each slide.

---

### 7. **Number of Recent Calls**

**Problem:** Implement a class that counts the number of calls made in the last 3000 milliseconds.

**Solution:**

```python
from collections import deque

class RecentCounter:
    def __init__(self):
        self.q = deque()

    def ping(self, t):
        self.q.append(t)
        while self.q and self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)

# Example
rc = RecentCounter()
print(rc.ping(1))    # 1
print(rc.ping(100))  # 2
print(rc.ping(3001)) # 3
print(rc.ping(3002)) # 3
```

**Explanation:**
Store timestamps in a queue and remove those outside the 3000 ms window on each ping.

---

### 8. **Longest Substring with At Most K Distinct Characters**

**Problem:** Find the length of the longest substring that contains at most `k` distinct characters.

**Solution:**

```python
def length_of_longest_substring_k_distinct(s, k):
    from collections import defaultdict
    left = 0
    max_len = 0
    count = defaultdict(int)

    for right in range(len(s)):
        count[s[right]] += 1
        while len(count) > k:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

# Example
s = "eceba"
k = 2
print(length_of_longest_substring_k_distinct(s, k))  # Output: 3 ("ece")
```

**Explanation:**
Use a sliding window with a hashmap to keep count of characters, shrink window when exceeding `k` distinct.

---

### 9. **Rearrange String k Distance Apart**

**Problem:** Rearrange characters in a string so that the same characters are at least `k` distance apart. Return any valid rearrangement or "" if impossible.

**Solution:**

```python
from collections import Counter, deque
import heapq

def rearrange_string(s, k):
    if k == 0:
        return s
    freq = Counter(s)
    max_heap = [(-count, char) for char, count in freq.items()]
    heapq.heapify(max_heap)
    wait_queue = deque()
    result = []

    while max_heap or wait_queue:
        if max_heap:
            count, char = heapq.heappop(max_heap)
            result.append(char)
            wait_queue
```

Certainly! Continuing the solution and explanation for problem 9, then finishing problem 10:

---

### 9. **Rearrange String k Distance Apart (continued)**

```python
from collections import Counter, deque
import heapq

def rearrange_string(s, k):
    if k == 0:
        return s
    freq = Counter(s)
    max_heap = [(-count, char) for char, count in freq.items()]
    heapq.heapify(max_heap)
    wait_queue = deque()  # stores (count, char, ready_time)
    result = []

    time = 0
    while max_heap or wait_queue:
        time += 1

        if max_heap:
            count, char = heapq.heappop(max_heap)
            result.append(char)
            # Decrease count (since count is negative)
            if count + 1 < 0:
                wait_queue.append((count + 1, char, time + k))
        else:
            # idle time, no char to append but waiting
            result.append('#')

        # Check if front of wait_queue is ready to be pushed back to heap
        if wait_queue and wait_queue[0][2] == time:
            heapq.heappush(max_heap, (wait_queue[0][0], wait_queue[0][1]))
            wait_queue.popleft()

    rearranged = ''.join(result)
    # If rearranged string length matches original, return it else ""
    return rearranged if len(rearranged.replace('#', '')) == len(s) else ""

# Example
s = "aabbcc"
k = 3
print(rearrange_string(s, k))  # Possible output: "abcabc"
```

**Explanation:**

* Use a max heap to always pick the most frequent character next.
* After placing a character, put it in a wait queue with a cooldown time.
* Only after `k` intervals, the character can be pushed back into the heap.
* If at any point we can't pick a character and still have to wait, we add idle time (`#`).
* Finally, if the constructed string length (excluding idles) equals original length, return it; otherwise, no valid rearrangement.

---

### 10. **Number of Islands II**

**Problem:** Given a grid of water and land initially all water, land is added one position at a time. After each addition, return the number of islands.

**Solution:**

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = 0  # number of islands

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            self.count -= 1
            return True
        return False

def num_islands2(m, n, positions):
    uf = UnionFind(m * n)
    grid = [[0] * n for _ in range(m)]
    res = []
    directions = [(1,0),(-1,0),(0,1),(0,-1)]

    for r, c in positions:
        if grid[r][c] == 1:
            res.append(uf.count)
            continue
        grid[r][c] = 1
        uf.count += 1
        idx = r * n + c

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            nidx = nr * n + nc
            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                uf.union(idx, nidx)
        res.append(uf.count)
    return res

# Example
positions = [[0,0],[0,1],[1,2],[2,1],[1,1]]
print(num_islands2(3, 3, positions))  # Output: [1,1,2,3,1]
```

**Explanation:**

* Use Union-Find (Disjoint Set Union) to merge adjacent lands into islands.
* After each addition of land, union it with neighboring lands if present.
* Track island count with union operations.
* Return count after each addition.

---

If you'd like, I can provide more problems or deeper explanations!
