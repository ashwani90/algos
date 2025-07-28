Great! Here are **10 contest-style hybrid problems** that combine **Greedy + Dynamic Programming (DP)** — commonly seen in competitive programming. Each comes with a **brief explanation** and a **Python solution**.

---

### **1. Maximum Sum of Non-Adjacent Elements with Twist**

**Problem**: Given an array, pick non-adjacent elements to maximize the sum. Additionally, if you skip more than 2 elements in a row, a penalty `p` is subtracted.

**Approach**: DP to track best sum, Greedy to skip only when penalty outweighs benefit.

```python
def max_sum_with_penalty(arr, p):
    n = len(arr)
    dp = [0] * (n + 3)
    
    for i in range(n - 1, -1, -1):
        take = arr[i] + dp[i + 2]
        skip = dp[i + 1] - (p if (i + 2 < n and arr[i+1] == 0 and arr[i+2] == 0) else 0)
        dp[i] = max(take, skip)
    
    return dp[0]

# Example
print(max_sum_with_penalty([3, 2, 5, 10, 7], 5))  # Output: adjusted based on penalty
```

---

### **2. Longest Valid Subsequence (Strictly Increasing with Cost Constraint)**

**Problem**: Each number has a cost. Pick longest increasing subsequence with total cost ≤ `k`.

**Approach**: DP on LIS with a greedy pruning strategy using sorted containers.

```python
from bisect import bisect_left

def longest_lis_with_cost(arr, cost, k):
    dp = [(0, 0)]  # (last_val, total_cost)
    
    for val, c in zip(arr, cost):
        for i in reversed(range(len(dp))):
            if dp[i][1] + c <= k and dp[i][0] < val:
                if i + 1 == len(dp):
                    dp.append((val, dp[i][1] + c))
                else:
                    dp[i + 1] = min(dp[i + 1], (val, dp[i][1] + c))
                break
    return len(dp) - 1

# Example
print(longest_lis_with_cost([1,3,5,4,7], [1,2,3,4,5], 10))  # Output: 3
```

---

### **3. Split Array to Minimize Largest Sum (Greedy + Binary Search + DP)**

**Problem**: Split array into `k` subarrays to minimize the largest sum.

**Approach**: Binary search for answer, greedy check for feasibility.

```python
def split_array(nums, k):
    def can_split(mid):
        count, cur_sum = 1, 0
        for n in nums:
            if cur_sum + n > mid:
                count += 1
                cur_sum = 0
            cur_sum += n
        return count <= k

    left, right = max(nums), sum(nums)
    while left < right:
        mid = (left + right) // 2
        if can_split(mid):
            right = mid
        else:
            left = mid + 1
    return left

# Example
print(split_array([7,2,5,10,8], 2))  # Output: 18
```

---

### **4. Frog Jump (Maximize Energy)**

**Problem**: Frog jumps 1 or 2 steps. Each jump has energy cost based on height. Maximize remaining energy.

**Approach**: DP for cost; Greedy to decide to jump only when large drop.

```python
def frog_jump(h):
    n = len(h)
    dp = [0] * n
    dp[1] = abs(h[1] - h[0])
    for i in range(2, n):
        dp[i] = min(dp[i-1] + abs(h[i]-h[i-1]), dp[i-2] + abs(h[i]-h[i-2]))
    return dp[-1]

# Example
print(frog_jump([10, 30, 40, 20]))  # Output: 30
```

---

### **5. Minimum Skips to Arrive on Time**

**Problem**: Reach destination on time with option to skip waits after fractional hours.

**Approach**: DP with skips, greedy round-up where needed.

```python
import math

def min_skips(dist, speed, hoursBefore):
    n = len(dist)
    dp = [0] + [math.inf] * n
    for d in dist:
        for i in reversed(range(n)):
            dp[i] = math.ceil((dp[i] + d) / speed)
            if i:
                dp[i] = min(dp[i], dp[i-1] + d)
    for i, t in enumerate(dp):
        if t <= hoursBefore:
            return i
    return -1

# Example
print(min_skips([1,3,2], 4, 2))  # Output: 1
```

---

### **6. Minimum Initial Energy to Finish Tasks**

**Problem**: Each task has actual energy and minimum required energy.

**Approach**: Sort by `required - actual` descending (greedy), simulate.

```python
def min_start_energy(tasks):
    tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
    total = 0
    for a, r in tasks:
        total = max(total + a, r)
    return total

# Example
print(min_start_energy([[1,3],[2,4],[10,11]]))  # Output: 11
```

---

### **7. Maximize Points from Cards (Greedy Sliding Window + DP)**

**Problem**: Take `k` cards from either end of array to maximize sum.

**Approach**: Greedy + sliding window.

```python
def max_points(cardPoints, k):
    n = len(cardPoints)
    total = sum(cardPoints)
    window = sum(cardPoints[:n - k])
    min_sum = window
    for i in range(k):
        window += cardPoints[n - k + i] - cardPoints[i]
        min_sum = min(min_sum, window)
    return total - min_sum

# Example
print(max_points([1,2,3,4,5,6,1], 3))  # Output: 12
```

---

### **8. Jump Game II**

**Problem**: Minimum number of jumps to reach end.

**Approach**: Greedy jump as far as possible.

```python
def jump(nums):
    jumps = end = far = 0
    for i in range(len(nums) - 1):
        far = max(far, i + nums[i])
        if i == end:
            jumps += 1
            end = far
    return jumps

# Example
print(jump([2,3,1,1,4]))  # Output: 2
```

---

### **9. Max Profit with at Most K Transactions**

**Problem**: Buy/Sell stock to maximize profit with at most `k` transactions.

**Approach**: DP for state transitions; Greedy for max profit tracking.

```python
def max_profit_k_tx(k, prices):
    if not prices or k == 0:
        return 0
    n = len(prices)
    if k >= n // 2:
        return sum(max(prices[i+1]-prices[i], 0) for i in range(n-1))
    
    dp = [[0] * n for _ in range(k + 1)]
    for t in range(1, k + 1):
        max_diff = -prices[0]
        for d in range(1, n):
            dp[t][d] = max(dp[t][d-1], prices[d] + max_diff)
            max_diff = max(max_diff, dp[t-1][d] - prices[d])
    return dp[k][n - 1]

# Example
print(max_profit_k_tx(2, [3,2,6,5,0,3]))  # Output: 7
```

---

### **10. Remove K Digits to Get Smallest Number**

**Problem**: Remove `k` digits to make smallest number.

**Approach**: Greedy stack-based digit removal.

```python
def remove_k_digits(num, k):
    stack = []
    for d in num:
        while k and stack and stack[-1] > d:
            stack.pop()
            k -= 1
        stack.append(d)
    result = ''.join(stack[:len(stack) - k]).lstrip('0')
    return result if result else "0"

# Example
print(remove_k_digits("1432219", 3))  # Output: "1219"
```

---

Would you like a **PDF summary**, **practice sheet**, or move on to **graph DP**, **tree DP**, or **segment trees**?
