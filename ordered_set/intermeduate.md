Sure! Here are **10 intermediate-level ordered set problems** with detailed **Python solutions and explanations**. We'll use `collections.OrderedDict` to simulate an ordered set, as Python doesn’t have a built-in `OrderedSet`.

---

## ✅ Intermediate Ordered Set Problems

---

### 1. **Keep first occurrence of each character in a string**

**Problem:**
Given a string, remove duplicates but keep the order of first occurrence.

```python
from collections import OrderedDict

def first_unique_characters(s):
    oset = OrderedDict()
    for c in s:
        oset[c] = None
    return ''.join(oset.keys())

print(first_unique_characters("banana"))
# Output: "ban"
```

**Explanation:**
Each character is stored once in insertion order.

---

### 2. **Check if two ordered sets are equal in order and elements**

```python
def are_ordered_sets_equal(s1, s2):
    return list(s1.keys()) == list(s2.keys())

oset1 = OrderedDict.fromkeys([1, 2, 3])
oset2 = OrderedDict.fromkeys([1, 2, 3])
oset3 = OrderedDict.fromkeys([3, 2, 1])
print(are_ordered_sets_equal(oset1, oset2))  # True
print(are_ordered_sets_equal(oset1, oset3))  # False
```

**Explanation:**
Convert to list and compare the order and values.

---

### 3. **Sliding Window Unique Elements**

**Problem:**
Given a list of integers and a window size `k`, print unique elements in each window preserving order.

```python
def sliding_window_uniques(arr, k):
    from collections import OrderedDict
    n = len(arr)
    for i in range(n - k + 1):
        window = OrderedDict()
        for j in range(i, i + k):
            window[arr[j]] = None
        print(list(window.keys()))

sliding_window_uniques([1, 2, 1, 3, 2], 3)
# Output:
# [1, 2]
# [2, 1, 3]
# [1, 3, 2]
```

**Explanation:**
Use an `OrderedDict` for each window to keep track of unique elements in order.

---

### 4. **Remove the last inserted element**

```python
def pop_last_inserted(oset):
    return oset.popitem(last=True)

oset = OrderedDict.fromkeys([1, 2, 3])
pop_last_inserted(oset)  # (3, None)
print(list(oset.keys()))  # [1, 2]
```

**Explanation:**
`.popitem(last=True)` removes the most recently inserted item.

---

### 5. **Move element to end**

```python
def move_to_end(oset, key):
    if key in oset:
        oset.move_to_end(key)
    return list(oset.keys())

oset = OrderedDict.fromkeys([1, 2, 3])
print(move_to_end(oset, 1))  # [2, 3, 1]
```

**Explanation:**
`move_to_end` shifts a specific element to the end, preserving uniqueness.

---

### 6. **Find all elements inserted before a given element**

```python
def elements_before(oset, key):
    result = []
    for k in oset:
        if k == key:
            break
        result.append(k)
    return result

oset = OrderedDict.fromkeys([1, 2, 3, 4])
print(elements_before(oset, 3))  # [1, 2]
```

**Explanation:**
Traverse until key is found.

---

### 7. **Find the K-th inserted unique element**

```python
def kth_inserted_element(oset, k):
    keys = list(oset.keys())
    if 0 <= k < len(keys):
        return keys[k]
    return None

oset = OrderedDict.fromkeys([5, 3, 9, 1])
print(kth_inserted_element(oset, 2))  # 9
```

**Explanation:**
Convert to list and return k-th element.

---

### 8. **Remove duplicates from list while preserving last occurrence**

```python
def remove_duplicates_last_occurrence(arr):
    seen = set()
    result = []
    for num in reversed(arr):
        if num not in seen:
            seen.add(num)
            result.append(num)
    return list(reversed(result))

print(remove_duplicates_last_occurrence([1, 2, 1, 3, 2]))
# Output: [1, 3, 2]
```

**Explanation:**
Traverse in reverse to preserve **last** occurrence, then reverse again.

---

### 9. **Ordered set difference maintaining order of first**

```python
def ordered_set_difference(a, b):
    return [x for x in a if x not in b]

a = [1, 2, 3, 4, 5]
b = {2, 4}
print(ordered_set_difference(a, b))  # [1, 3, 5]
```

**Explanation:**
Simple list filter while preserving order.

---

### 10. **Find common prefix of two ordered sets**

```python
def common_prefix(oset1, oset2):
    result = []
    for a, b in zip(oset1, oset2):
        if a == b:
            result.append(a)
        else:
            break
    return result

oset1 = [1, 2, 3, 4]
oset2 = [1, 2, 5]
print(common_prefix(oset1, oset2))  # [1, 2]
```

**Explanation:**
Iterate until mismatch.

---

Would you like me to continue with **advanced ordered set problems** or use other data structures like **trees**, **tries**, or **balanced BSTs** to implement ordered sets efficiently?
