Sure! Continuing with the explanation and solutions for advanced recursion problems:

---

### 9. **Interleaving String** (continued)

**Explanation (continued):**
Try to match the current character of s3 either with the current character of s1 or s2 recursively. Use memoization to avoid repeated computations.

---

### 10. **Count Unique BSTs (Catalan Number)**

**Problem:**
Given `n`, count how many structurally unique BSTs can be formed with values 1 to n.

**Solution:**

```python
def numTrees(n):
    memo = {}
    def count(start, end):
        if start > end:
            return 1
        if (start, end) in memo:
            return memo[(start, end)]
        total = 0
        for root in range(start, end + 1):
            left = count(start, root - 1)
            right = count(root + 1, end)
            total += left * right
        memo[(start, end)] = total
        return total

    return count(1, n)

print(numTrees(3))  # Output: 5
```

**Explanation:**
Pick each number as root, recursively count left and right subtree possibilities, multiply them, and sum for all roots. Memoization caches intermediate results.

---

If you'd like, I can provide more problems, solutions, or explanations on any other topic next!
