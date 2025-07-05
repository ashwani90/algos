Sure! Here are **10 intermediate-level recursion problems** along with detailed Python solutions and explanations.

---

### 1. **Generate all subsets (power set) of a set**

**Problem:**
Given a list, generate all subsets recursively.

**Solution:**

```python
def subsets(nums):
    result = []
    def backtrack(index, path):
        result.append(path[:])
        for i in range(index, len(nums)):
            path.append(nums[i])
            backtrack(i+1, path)
            path.pop()
    backtrack(0, [])
    return result

print(subsets([1,2,3]))
```

**Explanation:**
Use recursion to explore inclusion/exclusion of each element. Each recursive call decides whether to add the current element or not.

---

### 2. **Count ways to climb stairs (n steps, 1 or 2 steps at a time)**

**Problem:**
Find number of ways to reach the top of n stairs taking 1 or 2 steps.

**Solution:**

```python
def climb_stairs(n):
    if n == 0 or n == 1:
        return 1
    return climb_stairs(n-1) + climb_stairs(n-2)

print(climb_stairs(5))  # Output: 8
```

**Explanation:**
Ways to reach step n = ways to n-1 + ways to n-2. Base cases: 1 way to climb 0 or 1 step.

---

### 3. **Generate permutations of a list**

**Problem:**
Generate all permutations of a list recursively.

**Solution:**

```python
def permute(nums):
    result = []
    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
            return
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start+1)
            nums[start], nums[i] = nums[i], nums[start]
    backtrack(0)
    return result

print(permute([1,2,3]))
```

**Explanation:**
Swap elements recursively to create permutations, then backtrack to restore the original list.

---

### 4. **Find all combinations of numbers that sum to target**

**Problem:**
Given an array and a target sum, find all unique combinations of numbers that sum to target.

**Solution:**

```python
def combination_sum(candidates, target):
    result = []
    candidates.sort()
    def backtrack(start, target, path):
        if target == 0:
            result.append(path[:])
            return
        if target < 0:
            return
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                break
            path.append(candidates[i])
            backtrack(i, target - candidates[i], path)
            path.pop()
    backtrack(0, target, [])
    return result

print(combination_sum([2,3,6,7], 7))
```

**Explanation:**
Try including each candidate recursively, reducing target accordingly. Stop when target is zero or negative.

---

### 5. **Solve Maze (find path from start to end in grid)**

**Problem:**
Find any path from top-left to bottom-right in a grid moving only down or right.

**Solution:**

```python
def solve_maze(grid):
    rows, cols = len(grid), len(grid[0])
    path = []
    def backtrack(r, c):
        if r == rows or c == cols or grid[r][c] == 1:
            return False
        path.append((r, c))
        if r == rows-1 and c == cols-1:
            return True
        if backtrack(r+1, c) or backtrack(r, c+1):
            return True
        path.pop()
        return False
    if backtrack(0, 0):
        return path
    else:
        return []

maze = [[0,0,0],[0,1,0],[0,0,0]]
print(solve_maze(maze))
```

**Explanation:**
Try moving right or down recursively, backtracking if hitting walls or boundaries.

---

### 6. **Count number of unique paths in a grid**

**Problem:**
Count number of unique paths from top-left to bottom-right of an m x n grid.

**Solution:**

```python
def unique_paths(m, n):
    if m == 1 or n == 1:
        return 1
    return unique_paths(m-1, n) + unique_paths(m, n-1)

print(unique_paths(3, 3))  # Output: 6
```

**Explanation:**
Number of paths to (m,n) = paths to (m-1,n) + paths to (m,n-1). Base: 1 path when row or col is 1.

---

### 7. **Print all valid parentheses combinations**

**Problem:**
Print all combinations of n pairs of balanced parentheses.

**Solution:**

```python
def generate_parentheses(n):
    result = []
    def backtrack(open_count, close_count, path):
        if len(path) == 2 * n:
            result.append("".join(path))
            return
        if open_count < n:
            path.append('(')
            backtrack(open_count + 1, close_count, path)
            path.pop()
        if close_count < open_count:
            path.append(')')
            backtrack(open_count, close_count + 1, path)
            path.pop()
    backtrack(0, 0, [])
    return result

print(generate_parentheses(3))
```

**Explanation:**
Add '(' if still available; add ')' if it keeps string balanced. Recursion builds all valid sequences.

---

### 8. **Sum all numbers in a nested list**

**Problem:**
Given a nested list of integers, sum all integers recursively.

**Solution:**

```python
def sum_nested(lst):
    total = 0
    for elem in lst:
        if isinstance(elem, list):
            total += sum_nested(elem)
        else:
            total += elem
    return total

print(sum_nested([1, [2, [3, 4], 5], 6]))  # Output: 21
```

**Explanation:**
If element is a list, recurse into it, else add number to total.

---

### 9. **Print all root-to-leaf paths in a binary tree**

**Problem:**
Given a binary tree, print all root-to-leaf paths.

**Solution:**

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def print_paths(root):
    def dfs(node, path):
        if not node:
            return
        path.append(node.val)
        if not node.left and not node.right:
            print(path[:])
        else:
            dfs(node.left, path)
            dfs(node.right, path)
        path.pop()
    dfs(root, [])

# Example usage:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
print_paths(root)
```

**Explanation:**
Traverse tree, append node values to path, print path at leaf, backtrack after visiting children.

---

### 10. **Decode string with counts (e.g., "3\[a2\[c]]")**

**Problem:**
Decode a string with numbers indicating repetition.

**Solution:**

```python
def decode_string(s):
    stack_num = []
    stack_str = []
    current_str = ""
    current_num = 0
    
    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            stack_num.append(current_num)
            stack_str.append(current_str)
            current_str = ""
            current_num = 0
        elif char == ']':
            num = stack_num.pop()
            prev_str = stack_str.pop()
            current_str = prev_str + current_str * num
        else:
            current_str += char
    return current_str

print(decode_string("3[a2[c]]"))  # Output: accaccacc
```

**Explanation:**
Use stacks to store counts and strings when encountering '\['; build strings by popping stacks on ']'.

---

If you want me to explain any problem or code more deeply or provide further problems, just ask!
