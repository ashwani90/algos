Sure! Here are **10 intermediate-level stack problems** with detailed solutions and explanations:

---

### 1. **Basic Calculator II**

**Problem:**
Evaluate a string expression containing non-negative integers and operators `+`, `-`, `*`, `/`. The expression is guaranteed to be valid and should be evaluated according to operator precedence.

**Solution:**

```python
def calculate(s: str) -> int:
    stack = []
    num = 0
    sign = '+'
    s = s.replace(' ', '') + '+'  # add dummy operator to process last number
    
    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        else:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack[-1] = stack[-1] * num
            elif sign == '/':
                # truncate toward zero
                stack[-1] = int(stack[-1] / num)
            sign = char
            num = 0
    return sum(stack)

# Example
print(calculate("3+2*2"))  # Output: 7
```

**Explanation:**
Use a stack to store intermediate values. Apply multiplication and division immediately since they have higher precedence. At the end, sum all values.

---

### 2. **132 Pattern**

**Problem:**
Given an array of integers, find whether there exists a 132 pattern: i < j < k and nums\[i] < nums\[k] < nums\[j].

**Solution:**

```python
def find132pattern(nums):
    stack = []
    s3 = float('-inf')
    
    for num in reversed(nums):
        if num < s3:
            return True
        while stack and stack[-1] < num:
            s3 = stack.pop()
        stack.append(num)
    return False

# Example
print(find132pattern([3, 1, 4, 2]))  # True
```

**Explanation:**
Iterate from right to left. Use `s3` to track possible `nums[k]` in the pattern. Use a stack to keep candidates for `nums[j]`.

---

### 3. **Largest Rectangle in Histogram**

**Problem:**
Given heights of histogram bars, find the largest rectangle area.

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
Stack stores indices of ascending bars. When encountering lower height, compute area for bars popped.

---

### 4. **Simplify Path**

**Problem:**
Simplify a Unix-style path string by handling `"."`, `".."`, and redundant slashes.

**Solution:**

```python
def simplifyPath(path):
    stack = []
    parts = path.split('/')
    for part in parts:
        if part == '' or part == '.':
            continue
        if part == '..':
            if stack: stack.pop()
        else:
            stack.append(part)
    return '/' + '/'.join(stack)

# Example
print(simplifyPath("/a/./b/../../c/"))  # Output: "/c"
```

**Explanation:**
Use a stack to process directory names and handle special entries `"."` and `".."`.

---

### 5. **Evaluate Reverse Polish Notation**

**Problem:**
Evaluate an arithmetic expression in Reverse Polish Notation.

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
            else: stack.append(int(a / b))
        else:
            stack.append(int(token))
    return stack.pop()

# Example
print(evalRPN(["2","1","+","3","*"]))  # Output: 9
```

**Explanation:**
Use a stack to store numbers. When operator encountered, pop two operands and apply operator.

---

### 6. **Remove Duplicate Letters**

**Problem:**
Remove duplicate letters so that every letter appears once and result is smallest in lex order.

**Solution:**

```python
def removeDuplicateLetters(s):
    last_occurrence = {c:i for i,c in enumerate(s)}
    stack = []
    seen = set()
    
    for i, c in enumerate(s):
        if c not in seen:
            while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
                seen.remove(stack.pop())
            stack.append(c)
            seen.add(c)
    return ''.join(stack)

# Example
print(removeDuplicateLetters("cbacdcbc"))  # Output: "acdb"
```

**Explanation:**
Use a stack to build lex smallest sequence, popping when smaller letter comes and the popped letter appears later.

---

### 7. **Maximal Rectangle**

**Problem:**
Given a binary matrix, find the largest rectangle containing only 1's.

**Solution:**

```python
def maximalRectangle(matrix):
    if not matrix: return 0
    max_area = 0
    heights = [0] * len(matrix[0])
    
    for row in matrix:
        for i, val in enumerate(row):
            heights[i] = heights[i] + 1 if val == '1' else 0
        max_area = max(max_area, largestRectangleArea(heights))
    return max_area

def largestRectangleArea(heights):
    stack = []
    max_area = 0
    heights.append(0)
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            left = stack[-1] if stack else -1
            max_area = max(max_area, height * (i - left - 1))
        stack.append(i)
    return max_area

# Example
matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
print(maximalRectangle(matrix))  # Output: 6
```

**Explanation:**
Transform each row into a histogram and apply largest rectangle histogram solution.

---

### 8. **Trapping Rain Water**

**Problem:**
Given an elevation map, compute how much water it can trap after raining.

**Solution:**

```python
def trap(height):
    stack = []
    water = 0
    
    for i, h in enumerate(height):
        while stack and h > height[stack[-1]]:
            top = stack.pop()
            if not stack:
                break
            distance = i - stack[-1] - 1
            bounded_height = min(h, height[stack[-1]]) - height[top]
            water += distance * bounded_height
        stack.append(i)
    return water

# Example
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # Output: 6
```

**Explanation:**
Use a stack to find bounded areas where water can accumulate between bars.

---

### 9. **Online Stock Span**

**Problem:**
Calculate the stock span, i.e., for each day, find how many consecutive days before that day the price was less or equal.

**Solution:**

```python
class StockSpanner:
    def __init__(self):
        self.stack = []  # (price, span)

    def next(self, price):
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span

# Example
obj = StockSpanner()
print(obj.next(100))  # 1
print(obj.next(80))   # 1
print(obj.next(60))   # 1
print(obj.next(70))   # 2
print(obj.next(60))   # 1
print(obj.next(75))   # 4
print(obj.next(85))   # 6
```

**Explanation:**
Use stack to keep track of prices and their spans, merging spans for consecutive smaller prices.

---

### 10. **Basic Calculator**

**Problem:**
Evaluate a string expression containing `+`, `-`, `(`, `)` and non-negative integers.

**Solution:**

```python
def calculate(s):
    stack = []
    result = 0
    sign = 1
    num = 0
    
    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char in '+-':
            result += sign * num
            num = 0
            sign = 1 if char == '+' else -1
        elif char == '(':
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif char == ')':
            result += sign * num
            num = 0
            result
```

Sure! Continuing the solution and explanation for **Basic Calculator** problem and then finishing all 10 problems:

---

### 10. **Basic Calculator** (continued)

```python
def calculate(s):
    stack = []
    result = 0
    sign = 1
    num = 0
    
    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char in '+-':
            result += sign * num
            num = 0
            sign = 1 if char == '+' else -1
        elif char == '(':
            # Push current result and sign for '(' context
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif char == ')':
            # Finish current number before closing bracket
            result += sign * num
            num = 0
            # Pop sign and previous result
            prev_sign = stack.pop()
            prev_result = stack.pop()
            result = prev_result + prev_sign * result
    result += sign * num
    return result

# Example
print(calculate("(1+(4+5+2)-3)+(6+8)"))  # Output: 23
```

**Explanation:**

* Use `sign` to track current sign.
* Use a stack to save previous results and signs when encountering `'('`.
* Calculate partial results within parentheses and combine with outer expressions.

---

If you want, I can keep providing more problems in this or other topics! Just let me know.
