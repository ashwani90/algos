Absolutely! Here are **10 beginner-level stack problems** with detailed solutions and explanations:

---

### 1. **Valid Parentheses**

**Problem:** Given a string containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

**A string is valid if:**

* Open brackets are closed by the same type of brackets.
* Open brackets are closed in the correct order.

**Solution:**

```python
def isValid(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping.values():
            stack.append(char)
        else:
            if not stack or stack.pop() != mapping[char]:
                return False
    return not stack

# Example
print(isValid("()[]{}"))  # True
print(isValid("(]"))      # False
```

**Explanation:**
Use a stack to keep track of opening brackets. For each closing bracket, check if it matches the last opening bracket on the stack.

---

### 2. **Implement Stack Using Queues**

**Problem:** Implement a stack using queues with the operations: `push`, `pop`, `top`, and `empty`.

**Solution:**

```python
from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return not self.q

# Example
stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.top())   # 2
print(stack.pop())   # 2
print(stack.empty()) # False
```

**Explanation:**
By rotating the queue after each push, the newest element is always at the front, so pop and top operations are O(1).

---

### 3. **Min Stack**

**Problem:** Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

**Solution:**

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]

# Example
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())  # -3
minStack.pop()
print(minStack.top())     # 0
print(minStack.getMin())  # -2
```

**Explanation:**
Maintain a separate min\_stack to track minimums. When popping, remove from min\_stack if the popped element is minimum.

---

### 4. **Next Greater Element I**

**Problem:** Given two arrays `nums1` and `nums2`, find the next greater element for each element in `nums1` in `nums2`.

**Solution:**

```python
def nextGreaterElement(nums1, nums2):
    stack = []
    next_greater = {}
    for num in nums2:
        while stack and stack[-1] < num:
            next_greater[stack.pop()] = num
        stack.append(num)
    return [next_greater.get(x, -1) for x in nums1]

# Example
print(nextGreaterElement([4,1,2], [1,3,4,2]))  # [-1,3,-1]
```

**Explanation:**
Use a stack to keep track of decreasing elements and map each popped element to the next greater element.

---

### 5. **Daily Temperatures**

**Problem:** Given a list of daily temperatures, return a list where for each day, tells how many days you have to wait until a warmer temperature.

**Solution:**

```python
def dailyTemperatures(T):
    answer = [0] * len(T)
    stack = []  # indices of days
    
    for i, temp in enumerate(T):
        while stack and T[stack[-1]] < temp:
            prev_day = stack.pop()
            answer[prev_day] = i - prev_day
        stack.append(i)
    return answer

# Example
print(dailyTemperatures([73,74,75,71,69,72,76,73]))  
# Output: [1,1,4,2,1,1,0,0]
```

**Explanation:**
Use a stack to store indices of days with unresolved warmer days. When a warmer day is found, calculate the wait.

---

### 6. **Evaluate Reverse Polish Notation**

**Problem:** Evaluate the value of an arithmetic expression in Reverse Polish Notation.

**Solution:**

```python
def evalRPN(tokens):
    stack = []
    for token in tokens:
        if token in "+-*/":
            b = stack.pop()
            a = stack.pop()
            if token == '+': stack.append(a + b)
            elif token == '-': stack.append(a - b)
            elif token == '*': stack.append(a * b)
            else:  # division
                stack.append(int(a / b))
        else:
            stack.append(int(token))
    return stack.pop()

# Example
print(evalRPN(["2", "1", "+", "3", "*"]))  # (2+1)*3=9
```

**Explanation:**
Use a stack to push numbers and apply operators on top two elements when encountered.

---

### 7. **Simplify Path**

**Problem:** Given a Unix-style file path, simplify it (removing ".", "..", and extra slashes).

**Solution:**

```python
def simplifyPath(path):
    stack = []
    parts = path.split('/')
    for part in parts:
        if part == '..':
            if stack: stack.pop()
        elif part and part != '.':
            stack.append(part)
    return '/' + '/'.join(stack)

# Example
print(simplifyPath("/a/./b/../../c/"))  # Output: "/c"
```

**Explanation:**
Split by '/', use a stack to handle directory names, pop for "..", ignore "." or empty parts.

---

### 8. **Largest Rectangle in Histogram**

**Problem:** Find the largest rectangle area in a histogram represented by an array of bar heights.

**Solution:**

```python
def largestRectangleArea(heights):
    stack = []
    max_area = 0
    heights.append(0)  # Sentinel

    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            left = stack[-1] if stack else -1
            max_area = max(max_area, height * (i - left - 1))
        stack.append(i)
    return max_area

# Example
print(largestRectangleArea([2,1,5,6,2,3]))  # Output: 10
```

**Explanation:**
Use a stack to track ascending bars, calculate area whenever a lower height is found.

---

### 9. **Remove K Digits**

**Problem:** Given a number as a string and an integer k, remove k digits to make the smallest possible number.

**Solution:**

```python
def removeKdigits(num, k):
    stack = []
    for digit in num:
        while k and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    # If k still > 0, remove from end
    final_stack = stack[:-k] if k else stack
    # Remove leading zeros
    return ''.join(final_stack).lstrip('0') or "0"

# Example
print(removeKdigits("1432219", 3))  # Output: "1219"
```

**Explanation:**
Use a stack to greedily remove larger digits before smaller digits to get the smallest number.

---

### 10. **Decode String**

**Problem:** Given an encoded string like `"3[a2[c]]"`, decode it to `"accaccacc"`.

**Solution:**

```python
def decodeString(s):
    stack = []
    current_num = 0
    current_str = ''

    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            stack.append((current_str, current_num))
            current_str = ''
            current_num = 0
        elif char == ']':
            prev_str, num = stack.pop()
            current_str = prev_str + current_str * num
        else:
            current_str += char
    return current_str

# Example
print(decodeString("3[a2[c]]"))  # Output: "accaccacc"
```

**Explanation:**
Use stack to save the current string and number when encountering `[`. When `]` is found, decode the substring accordingly.

---

If you'd like, I can provide solutions to more stack problems or problems on other topics!
