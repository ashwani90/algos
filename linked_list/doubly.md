Here are **10 doubly linked list problems** along with their **Python solutions and detailed explanations**. These problems range from basic operations to more complex manipulations involving `prev` and `next` pointers.

---

### **1. Insert Node at Head of Doubly Linked List**

**Problem:** Insert a node at the beginning of a doubly linked list.

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

def insert_at_head(head, val):
    new_node = Node(val)
    new_node.next = head
    if head:
        head.prev = new_node
    return new_node
```

**Explanation:** Create a new node and set its `next` to the current head. Update the old head's `prev`.

---

### **2. Insert Node at Tail**

```python
def insert_at_tail(head, val):
    new_node = Node(val)
    if not head:
        return new_node

    curr = head
    while curr.next:
        curr = curr.next

    curr.next = new_node
    new_node.prev = curr
    return head
```

**Explanation:** Traverse to the end, insert the new node, and update pointers.

---

### **3. Delete Node from Doubly Linked List**

```python
def delete_node(head, node_to_delete):
    if node_to_delete.prev:
        node_to_delete.prev.next = node_to_delete.next
    else:
        head = node_to_delete.next
    if node_to_delete.next:
        node_to_delete.next.prev = node_to_delete.prev
    return head
```

**Explanation:** Reconnect the previous and next nodes, adjusting head if needed.

---

### **4. Reverse a Doubly Linked List**

```python
def reverse_doubly_linked_list(head):
    curr = head
    temp = None
    while curr:
        temp = curr.prev
        curr.prev = curr.next
        curr.next = temp
        curr = curr.prev
    return temp.prev if temp else head
```

**Explanation:** Swap `next` and `prev` pointers at each step. Return the new head.

---

### **5. Find Pairs with Given Sum**

Given a sorted doubly linked list, find pairs with a given sum.

```python
def find_pairs_with_sum(head, target):
    res = []
    start = head
    end = head
    while end.next:
        end = end.next

    while start != end and start.prev != end:
        s = start.val + end.val
        if s == target:
            res.append((start.val, end.val))
            start = start.next
            end = end.prev
        elif s < target:
            start = start.next
        else:
            end = end.prev
    return res
```

**Explanation:** Use two pointers from both ends of the list, moving based on the sum.

---

### **6. Check if a Doubly Linked List is Palindrome**

```python
def is_palindrome(head):
    if not head or not head.next:
        return True

    left = head
    right = head
    while right.next:
        right = right.next

    while left != right and left.prev != right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.prev

    return True
```

**Explanation:** Use two pointers and compare from both ends inward.

---

### **7. Flatten a Multilevel Doubly Linked List**

(Also from earlier, but relevant here.)

```python
def flatten(head):
    if not head:
        return None

    def dfs(node):
        curr = node
        last = node

        while curr:
            next_node = curr.next
            if curr.child:
                child_head = curr.child
                child_tail = dfs(child_head)

                curr.next = child_head
                child_head.prev = curr
                child_tail.next = next_node
                if next_node:
                    next_node.prev = child_tail
                curr.child = None
                last = child_tail
            else:
                last = curr
            curr = next_node
        return last

    dfs(head)
    return head
```

**Explanation:** DFS to flatten children recursively into main list.

---

### **8. Rotate Doubly Linked List by K nodes**

```python
def rotate_doubly_linked_list(head, k):
    if not head or k == 0:
        return head

    curr = head
    count = 1
    while count < k and curr:
        curr = curr.next
        count += 1

    if not curr:
        return head

    kth_node = curr
    new_head = kth_node.next
    if new_head:
        new_head.prev = None
    kth_node.next = None

    tail = new_head
    while tail and tail.next:
        tail = tail.next

    if tail:
        tail.next = head
        head.prev = tail

    return new_head if new_head else head
```

**Explanation:** Break after k nodes, append front to end, and reassign pointers.

---

### **9. Convert Binary Tree to Doubly Linked List**

In-order convert binary tree to DLL.

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def btree_to_dll(root):
    def inorder(node):
        nonlocal last, head
        if not node:
            return
        inorder(node.left)
        if last:
            last.right = node
            node.left = last
        else:
            head = node
        last = node
        inorder(node.right)

    head = last = None
    inorder(root)
    return head
```

**Explanation:** Inorder traversal links tree nodes into a doubly linked list.

---

### **10. Merge Two Sorted Doubly Linked Lists**

```python
def merge_sorted_dll(a, b):
    if not a:
        return b
    if not b:
        return a

    if a.val < b.val:
        a.next = merge_sorted_dll(a.next, b)
        if a.next:
            a.next.prev = a
        return a
    else:
        b.next = merge_sorted_dll(a, b.next)
        if b.next:
            b.next.prev = b
        return b
```

**Explanation:** Recursively merge lists based on node values and maintain both `next` and `prev`.

---

Would you like a set of **doubly linked list interview-style challenges**, or transition into **circular** or **custom cache-style structures** (like LRU)?
Great! Let's continue with **10 more advanced doubly linked list problems** that touch on practical applications like LRU cache, custom deque design, memory-efficient traversals, and more.

---

### **11. Implement LRU (Least Recently Used) Cache**

**Problem:** Implement an LRU cache using a doubly linked list + hashmap.

```python
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        node.prev = p
        node.next = self.tail
        self.tail.prev = node

    def get(self, key):
        if key in self.map:
            self._remove(self.map[key])
            self._add(self.map[key])
            return self.map[key].val
        return -1

    def put(self, key, val):
        if key in self.map:
            self._remove(self.map[key])
        node = Node(key, val)
        self._add(node)
        self.map[key] = node

        if len(self.map) > self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.map[lru.key]
```

**Explanation:** Doubly linked list manages order of usage; hashmap provides `O(1)` access.

---

### **12. Design a Deque (Double Ended Queue)**

```python
class MyDeque:
    def __init__(self):
        self.head = self.tail = None

    def push_front(self, val):
        node = Node(val)
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node
        if not self.tail:
            self.tail = node

    def push_back(self, val):
        node = Node(val)
        node.prev = self.tail
        if self.tail:
            self.tail.next = node
        self.tail = node
        if not self.head:
            self.head = node

    def pop_front(self):
        if not self.head:
            return None
        val = self.head.val
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return val

    def pop_back(self):
        if not self.tail:
            return None
        val = self.tail.val
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        return val
```

**Explanation:** Manual implementation of deque using doubly linked list.

---

### **13. Remove All Duplicates from Sorted Doubly Linked List**

```python
def remove_duplicates(head):
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
            if curr.next:
                curr.next.prev = curr
        else:
            curr = curr.next
    return head
```

**Explanation:** Sequentially remove nodes with the same value as current.

---

### **14. Convert DLL to Balanced BST**

```python
class DLLToBST:
    def __init__(self, head):
        self.head = head

    def count_nodes(self, node):
        count = 0
        while node:
            count += 1
            node = node.next
        return count

    def convert(self, n):
        if n <= 0:
            return None

        left = self.convert(n // 2)
        root = TreeNode(self.head.val)
        root.left = left
        self.head = self.head.next
        root.right = self.convert(n - n // 2 - 1)
        return root

    def to_bst(self):
        n = self.count_nodes(self.head)
        return self.convert(n)
```

**Explanation:** In-order construction of BST using DLL node traversal.

---

### **15. Rearrange Doubly Linked List Alternating Ends**

**Problem:** Reorder DLL like first -> last -> second -> second-last...

```python
def reorder_dll(head):
    if not head:
        return None

    tail = head
    while tail.next:
        tail = tail.next

    dummy = Node(0)
    curr = dummy

    while head != tail and head.prev != tail:
        curr.next = head
        head.prev = curr
        head = head.next

        curr = curr.next
        curr.next = tail
        tail.prev = curr
        tail = tail.prev
        curr = curr.next

    if head == tail:
        curr.next = head
        head.prev = curr
        curr = curr.next

    curr.next = None
    return dummy.next
```

**Explanation:** Alternate selection from start and end using two pointers.

---

### **16. Detect and Remove Loop in Doubly Linked List**

```python
def detect_loop(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

**Explanation:** Floyd’s cycle detection works even in DLLs if `next` has loop.

---

### **17. Find Middle of Doubly Linked List**

```python
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.val if slow else None
```

**Explanation:** Classic two-pointer method.

---

### **18. Swap K-th Node from Start and End**

```python
def swap_kth(head, k):
    n = 0
    curr = head
    while curr:
        n += 1
        curr = curr.next

    if k > n:
        return head

    front = end = head
    for _ in range(k - 1):
        front = front.next
    for _ in range(n - k):
        end = end.next

    if front == end:
        return head

    front.val, end.val = end.val, front.val
    return head
```

**Explanation:** Swap the values of k-th from start and end.

---

### **19. Clone a Doubly Linked List with Random Pointer**

```python
class RandomNode:
    def __init__(self, val):
        self.val = val
        self.next = self.prev = self.random = None

def clone_list(head):
    if not head:
        return None

    curr = head
    while curr:
        copy = RandomNode(curr.val)
        copy.next = curr.next
        curr.next = copy
        curr = copy.next

    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next

    dummy = RandomNode(0)
    copy_curr = dummy
    curr = head
    while curr:
        copy = curr.next
        curr.next = copy.next
        copy_curr.next = copy
        copy_curr = copy
        curr = curr.next

    return dummy.next
```

**Explanation:** Three-pass trick to clone random pointer DLL in `O(n)` time and space.

---

### **20. Remove N-th Node from End**

```python
def remove_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head
    head.prev = dummy

    first = second = dummy
    for _ in range(n):
        if second.next:
            second = second.next

    while second.next:
        first = first.next
        second = second.next

    to_delete = first.next
    first.next = to_delete.next
    if to_delete.next:
        to_delete.next.prev = first

    return dummy.next
```

**Explanation:** Use two pointers to reach the (N-th from end) node and remove it.

---

Would you like:

* Practice problems and solutions involving **circular doubly linked lists**?
* **Time complexity analysis** of operations?
* Or move on to another data structure (e.g., trees, graphs, tries)?
