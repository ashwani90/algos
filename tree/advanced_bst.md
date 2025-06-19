Great! Let's continue with the solutions and explanations for **problems 13–20** from the advanced BST list.

Great! Here are **20 advanced problems on Binary Search Trees (BSTs)** along with problem statements, core ideas, and brief explanations of how to approach each. These problems cover advanced topics like in-order threading, dynamic updates, augmenting BSTs, balanced BSTs (AVL/Red-Black), and even some interval or persistent tree tricks.

---

### 🧠 **Advanced Binary Search Tree Problems**

---

### **1. Construct BST from Preorder Traversal**

* **Problem**: Given a preorder traversal, construct a BST.
* **Idea**: Use bounds to maintain valid ranges.
* ✅ `O(n)` recursive construction.

---

### **2. BST to Sorted Circular Doubly Linked List**

* **Problem**: Convert BST to a circular DLL in-place.
* **Idea**: Inorder traversal + threading.

---

### **3. Recover BST with Two Swapped Nodes**

* **Problem**: Two nodes in a BST were swapped by mistake. Restore it.
* **Idea**: Inorder traversal + identify 2 misplaced nodes.

---

### **4. Serialize and Deserialize BST**

* **Problem**: Serialize a BST with minimal space.
* **Idea**: Use preorder for serialization; reconstruct with bounds.

---

### **5. Count BST Nodes Within Range \[L, R]**

* **Problem**: Count number of nodes whose values fall within a range.
* **Idea**: Inorder traversal with pruning.

---

### **6. Kth Smallest Element in BST (Dynamic Updates)**

* **Problem**: BST with frequent insert/delete and kth queries.
* **Idea**: Augment BST nodes with subtree size.
* ✅ Requires custom BST or AVL/Segment Tree.

---

### **7. Median in a Stream using BST**

* **Problem**: Insert values one by one, return median at each step.
* **Idea**: Self-balancing BST or two heaps.

---

### **8. Construct BST from Postorder Traversal**

* **Idea**: Traverse reversed postorder, use min/max bounds.

---

### **9. Convert Sorted DLL to Balanced BST**

* **Problem**: DLL is sorted. Convert it to height-balanced BST.
* **Idea**: In-order construction recursively.

---

### **10. Largest BST Subtree in Binary Tree**

* **Problem**: Given a binary tree, find the largest subtree that is a valid BST.
* **Idea**: Post-order recursion with min/max size validation.

---

### **11. Count Number of Unique BSTs (Catalan Number)**

* **Problem**: Count unique BSTs with `n` nodes.
* **Idea**: `dp[n] = sum(dp[i] * dp[n-i-1])`

---

### **12. Convert Binary Tree to BST Keeping Structure**

* **Problem**: Convert tree to BST without changing its structure.
* **Idea**: Inorder traversal, sort values, refill in-order.

---

### **13. Predecessor and Successor in BST**

* **Problem**: Find in-order predecessor and successor for a key.
* **Idea**: Recursive search with tracking.

---

### **14. Validate BST with Duplicates on Left Allowed**

* **Problem**: Modify BST check to allow duplicates on the left.
* **Idea**: Adjust comparison bounds.

---

### **15. BST Iterator (Inorder, O(h) space)**

* **Problem**: Implement `next()` and `hasNext()` for BST traversal.
* **Idea**: Use a stack to simulate recursion.

---

### **16. Persistent BST (Versioned Insertions and Queries)**

* **Problem**: Support multiple versions of BST with insertions.
* **Idea**: Copy-on-write + structural sharing.
* ✅ Functional programming style.

---

### **17. Interval Tree using BST**

* **Problem**: Insert intervals, support overlap query.
* **Idea**: Augment BST with max endpoint of subtree.

---

### **18. Range Sum in BST**

* **Problem**: Find sum of values in range \[L, R].
* **Idea**: Pruned DFS based on BST property.

---

### **19. Rebuild BST from Inorder and Level Order**

* **Problem**: Construct BST from level-order and inorder.
* **Idea**: Use a hash map of inorder indices + recursion.

---

### **20. Merge Two BSTs into One Balanced BST**

* **Problem**: Merge two BSTs into one balanced BST.
* **Idea**:

  * Inorder of both → merge arrays → build BST

---

### ✅ Next Steps

Would you like:

* Full solutions for specific ones from this list?
* A set of these in Leetcode-style format?
* Practice progression from intermediate → advanced BSTs?
* Challenges using AVL/Red-Black Tree augmentations?

Let me know what direction you'd like next (e.g., solve top 5 from above, build your own BST class, etc.)!

---

### **13. Predecessor and Successor in BST**

**Problem**: For a given key, find the in-order predecessor and successor.

```python
def find_pre_suc(root, key):
    pred, succ = None, None
    while root:
        if root.val < key:
            pred = root
            root = root.right
        elif root.val > key:
            succ = root
            root = root.left
        else:
            if root.left:
                t = root.left
                while t.right:
                    t = t.right
                pred = t
            if root.right:
                t = root.right
                while t.left:
                    t = t.left
                succ = t
            break
    return (pred.val if pred else None, succ.val if succ else None)
```

---

### **14. Validate BST with Duplicates Allowed on Left**

**Problem**: Validate BST where duplicates are allowed on the left subtree.

```python
def is_valid_bst_with_duplicates(root):
    def helper(node, low, high):
        if not node:
            return True
        if not (low <= node.val < high):
            return False
        return helper(node.left, low, node.val + 1) and helper(node.right, node.val + 1, high)
    return helper(root, float('-inf'), float('inf'))
```

---

### **15. BST Iterator (Inorder, O(h) space)**

**Problem**: Implement `next()` and `hasNext()` methods for BST traversal.

```python
class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        node = self.stack.pop()
        if node.right:
            self._leftmost_inorder(node.right)
        return node.val

    def hasNext(self):
        return len(self.stack) > 0
```

---

### **16. Persistent BST (Versioned Insertions)**

**Problem**: Maintain multiple versions of a BST where each insert creates a new version.

**Note**: We'll clone nodes during insert to maintain persistence.

```python
class PersistentNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def insert_persistent(root, val):
    if not root:
        return PersistentNode(val)
    new_root = PersistentNode(root.val)
    if val < root.val:
        new_root.left = insert_persistent(root.left, val)
        new_root.right = root.right
    else:
        new_root.right = insert_persistent(root.right, val)
        new_root.left = root.left
    return new_root
```

---

### **17. Interval Tree using BST**

**Problem**: Insert intervals and query for overlapping intervals.

```python
class IntervalNode:
    def __init__(self, interval):
        self.interval = interval
        self.max = interval[1]
        self.left = self.right = None

def insert_interval(root, interval):
    if not root:
        return IntervalNode(interval)
    if interval[0] < root.interval[0]:
        root.left = insert_interval(root.left, interval)
    else:
        root.right = insert_interval(root.right, interval)
    root.max = max(root.max, interval[1])
    return root

def overlap(interval1, interval2):
    return interval1[0] <= interval2[1] and interval2[0] <= interval1[1]

def search_overlap(root, target):
    if not root:
        return None
    if overlap(root.interval, target):
        return root.interval
    if root.left and root.left.max >= target[0]:
        return search_overlap(root.left, target)
    return search_overlap(root.right, target)
```

---

### **18. Range Sum in BST**

**Problem**: Return the sum of all values in a BST in the range \[L, R].

```python
def range_sum_bst(root, L, R):
    if not root:
        return 0
    if root.val < L:
        return range_sum_bst(root.right, L, R)
    elif root.val > R:
        return range_sum_bst(root.left, L, R)
    return root.val + range_sum_bst(root.left, L, R) + range_sum_bst(root.right, L, R)
```

---

### **19. Rebuild BST from Inorder and Level Order**

**Idea**: Use level order for root selection, and inorder for left/right subtrees.

```python
def build_bst_from_inorder_level(inorder, level_order):
    if not inorder:
        return None
    for x in level_order:
        if x in inorder:
            root_val = x
            break
    root = TreeNode(root_val)
    idx = inorder.index(root_val)
    left_inorder = inorder[:idx]
    right_inorder = inorder[idx+1:]
    root.left = build_bst_from_inorder_level(left_inorder, level_order)
    root.right = build_bst_from_inorder_level(right_inorder, level_order)
    return root
```

---

### **20. Merge Two BSTs into One Balanced BST**

**Idea**: In-order traverse both trees to get sorted arrays, merge them, and build BST.

```python
def inorder(root, arr):
    if root:
        inorder(root.left, arr)
        arr.append(root.val)
        inorder(root.right, arr)

def merge(arr1, arr2):
    return sorted(arr1 + arr2)

def sorted_array_to_bst(arr):
    if not arr:
        return None
    mid = len(arr) // 2
    root = TreeNode(arr[mid])
    root.left = sorted_array_to_bst(arr[:mid])
    root.right = sorted_array_to_bst(arr[mid+1:])
    return root

def merge_bsts(root1, root2):
    arr1, arr2 = [], []
    inorder(root1, arr1)
    inorder(root2, arr2)
    merged = merge(arr1, arr2)
    return sorted_array_to_bst(merged)
```

---

That completes the solutions for all **20 advanced BST problems**!
Would you like a printable summary or another set of problems (e.g. AVL, Segment Trees, or problems involving tree traversals)?
