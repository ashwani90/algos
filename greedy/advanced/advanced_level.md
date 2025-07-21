Great! Let’s continue with **10 more advanced greedy problems**, focusing on trickier edge cases, hybrid techniques, and competitive programming-style challenges — each with a **detailed explanation** and **Python solution**.

---

## 🔥 10 More Advanced Greedy Problems (Part 3)

---

### **1. Minimum Cost to Hire K Workers**

**Problem**: Given quality and wage of workers, hire exactly `K` workers with the minimum cost, keeping the wage-to-quality ratio same.

**Greedy Idea**: Sort by ratio, maintain min-heap for smallest total quality.

```python
import heapq

def mincost_to_hire_workers(quality, wage, K):
    workers = sorted([(w / q, q) for q, w in zip(quality, wage)])
    res, total_quality = float('inf'), 0
    heap = []

    for ratio, q in workers:
        heapq.heappush(heap, -q)
        total_quality += q
        if len(heap) > K:
            total_quality += heapq.heappop(heap)
        if len(heap) == K:
            res = min(res, total_quality * ratio)
    return res

# Example
print(mincost_to_hire_workers([10,20,5], [70,50,30], 2))  # Output: 105.0
```

---

### **2. Maximum Number of Events Attended**

**Problem**: Attend as many events as possible. Each event has a start and end day.

**Greedy Idea**: Sort events by start time and use a min-heap for current available end times.

```python
import heapq

def max_events(events):
    events.sort()
    heap = []
    i = res = day = 0
    n = len(events)

    while i < n or heap:
        if not heap:
            day = events[i][0]
        while i < n and events[i][0] <= day:
            heapq.heappush(heap, events[i][1])
            i += 1
        heapq.heappop(heap)
        res += 1
        day += 1
    return res

# Example
print(max_events([[1,2],[2,3],[3,4]]))  # Output: 3
```

---

### **3. Partition Labels**

**Problem**: Partition a string into as many parts as possible so each letter appears in at most one part.

**Greedy Idea**: Track last occurrence of each character and cut when all chars in current part are within bounds.

```python
def partition_labels(s):
    last = {c: i for i, c in enumerate(s)}
    res = []
    j = anchor = 0

    for i, c in enumerate(s):
        j = max(j, last[c])
        if i == j:
            res.append(i - anchor + 1)
            anchor = i + 1
    return res

# Example
print(partition_labels("ababcbacadefegdehijhklij"))  # Output: [9, 7, 8]
```

---

### **4. Minimum Taps to Water a Garden**

**Problem**: Find minimum number of taps to open to water a garden from 0 to `n`.

**Greedy Idea**: Similar to Jump Game II. Convert to interval covering.

```python
def min_taps(n, ranges):
    intervals = []
    for i, r in enumerate(ranges):
        intervals.append((max(0, i - r), min(n, i + r)))
    intervals.sort()

    i = res = end = far = 0
    while end < n:
        while i < len(intervals) and intervals[i][0] <= end:
            far = max(far, intervals[i][1])
            i += 1
        if end == far:
            return -1
        end = far
        res += 1
    return res

# Example
print(min_taps(5, [3,4,1,1,0,0]))  # Output: 1
```

---

### **5. Non-overlapping Intervals**

**Problem**: Remove the minimum number of intervals to make the rest non-overlapping.

**Greedy Idea**: Sort by end time and count overlaps.

```python
def erase_overlap_intervals(intervals):
    intervals.sort(key=lambda x: x[1])
    end = float('-inf')
    count = 0

    for interval in intervals:
        if interval[0] >= end:
            end = interval[1]
        else:
            count += 1
    return count

# Example
print(erase_overlap_intervals([[1,2],[2,3],[3,4],[1,3]]))  # Output: 1
```

---

### **6. Candy Distribution**

**Problem**: Distribute candies to children with ratings, where children with higher ratings get more candies.

**Greedy Idea**: Two passes — left to right and right to left.

```python
def candy(ratings):
    n = len(ratings)
    candies = [1] * n

    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    for i in reversed(range(n - 1)):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    return sum(candies)

# Example
print(candy([1,0,2]))  # Output: 5
```

---

### **7. Boats to Save People**

**Problem**: Each boat can carry at most 2 people with weight limit. Return min number of boats.

**Greedy Idea**: Two pointers on sorted array, pair heaviest with lightest.

```python
def num_rescue_boats(people, limit):
    people.sort()
    i, j = 0, len(people) - 1
    boats = 0

    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
        boats += 1
    return boats

# Example
print(num_rescue_boats([3,2,2,1], 3))  # Output: 3
```

---

### **8. Task Scheduler**

**Problem**: Given tasks and cooldown time `n`, return least interval to finish all.

**Greedy Idea**: Max-heap of task counts, simulate each cycle.

```python
from collections import Counter
import heapq

def least_interval(tasks, n):
    counter = Counter(tasks)
    heap = [-cnt for cnt in counter.values()]
    heapq.heapify(heap)
    
    time = 0
    while heap:
        temp = []
        for _ in range(n + 1):
            if heap:
                temp.append(heapq.heappop(heap))
        for t in temp:
            if t + 1 != 0:
                heapq.heappush(heap, t + 1)
        time += n + 1 if heap else len(temp)
    return time

# Example
print(least_interval(["A","A","A","B","B","B"], 2))  # Output: 8
```

---

### **9. Minimum Number of Arrows to Burst Balloons**

**Problem**: Balloons are intervals. Find min arrows to burst all.

**Greedy Idea**: Sort by end point and burst as many as possible.

```python
def find_min_arrow_shots(points):
    points.sort(key=lambda x: x[1])
    arrows = 0
    end = float('-inf')

    for p in points:
        if p[0] > end:
            arrows += 1
            end = p[1]
    return arrows

# Example
print(find_min_arrow_shots([[10,16],[2,8],[1,6],[7,12]]))  # Output: 2
```

---

### **10. Minimum Number of Coins for Change (non-standard denominations)**

**Problem**: Given a coin set, find min number of coins to make change. (Only works greedily if denominations are canonical.)

**Greedy Idea**: Try largest coin first (only works correctly for canonical systems like US currency).

```python
def min_coins(coins, amount):
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        take = amount // coin
        count += take
        amount -= coin * take
    return count if amount == 0 else -1

# Example (canonical coins)
print(min_coins([1, 5, 10, 25], 63))  # Output: 6
```

---

Would you like next:

* 10 **real contest-style greedy + DP** hybrid problems?
* Or switch to another algorithm (e.g., graphs, trees, segment trees)?
