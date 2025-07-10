Here are **10 advanced-level linked list problems** with **detailed Python solutions and explanations**. These cover complex operations, in-place algorithms, deep copies, and cycle-related challenges.

---

### **1. Copy List with Random Pointer**

Each node has a `random` pointer in addition to `next`. Return a deep copy.

```python
class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def copy_random_list(head):
    if not head:
        return None

    # Step 1: Clone each node and insert it
    curr = head
    while curr:
        new_node = Node(curr.val, curr.next, None)
        curr.next = new_node
        curr = new_node.next

    # Step 2: Set random pointers
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next

    # Step 3: Separate the lists
    curr = head
    copy = head.next
    copy_head = copy
    while curr:
        curr.next = curr.next.next
        copy.next = copy.next.next if copy.next else None
        curr = curr.next
        copy = copy.next

    return copy_head
```

**Explanation:** Clone and insert nodes in between originals, set `.random` pointers, then split the list.

---

### **2. Reverse Nodes in k-Group**

```python
def reverse_k_group(head, k):
    def get_kth(curr, k):
        while curr and k:
            curr = curr.next
            k -= 1
        return curr

    dummy = ListNode(0)
    dummy.next = head
    group_prev = dummy

    while True:
        kth = get_kth(group_prev, k)
        if not kth:
            break
        group_next = kth.next

        prev, curr = kth.next, group_prev.next
        while curr != group_next:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        temp = group_prev.next
        group_prev.next = kth
        group_prev = temp

    return dummy.next
```

**Explanation:** Reverse every k nodes in-place by first finding the kth node and reversing the segment.

---

### **3. Flatten a Multilevel Doubly Linked List**

```python
class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

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

**Explanation:** Use DFS to flatten the child lists recursively into the main list.

---

### **4. Linked List Cycle II (Return Cycle Start)**

*(Same as intermediate #3 but fits advanced due to logic)*

---

### **5. Find Duplicate Number (Floyd’s Tortoise and Hare on Array)**

Use linked list cycle detection idea on array-based list.

```python
def find_duplicate(nums):
    slow = fast = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    fast = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow
```

**Explanation:** The array is viewed as a linked list where `nums[i]` is the "next" pointer.

---

### **6. Reorder List**

```python
def reorder_list(head):
    if not head:
        return

    # Step 1: Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse second half
    prev = None
    curr = slow.next
    slow.next = None
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    # Step 3: Merge halves
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2
```

**Explanation:** Find the middle, reverse the second half, then merge.

---

### **7. Convert Sorted List to BST**

```python
def sorted_list_to_bst(head):
    def find_size(node):
        size = 0
        while node:
            node = node.next
            size += 1
        return size

    def convert(l, r):
        nonlocal head
        if l > r:
            return None
        mid = (l + r) // 2
        left = convert(l, mid - 1)
        node = TreeNode(head.val)
        node.left = left
        head = head.next
        node.right = convert(mid + 1, r)
        return node

    size = find_size(head)
    return convert(0, size - 1)
```

**Explanation:** In-order construct BST using linked list, similar to array to BST.

---

### **8. Remove Zero Sum Consecutive Nodes**

```python
def remove_zero_sum_sublists(head):
    dummy = ListNode(0)
    dummy.next = head
    prefix = 0
    seen = {}

    curr = dummy
    while curr:
        prefix += curr.val
        seen[prefix] = curr
        curr = curr.next

    prefix = 0
    curr = dummy
    while curr:
        prefix += curr.val
        curr.next = seen[prefix].next
        curr = curr.next

    return dummy.next
```

**Explanation:** Use prefix sum and map it to nodes. If the same prefix reoccurs, nodes in between sum to 0.

---

### **9. Split Linked List into K Parts**

```python
def split_list_to_parts(head, k):
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next

    part_size, remainder = divmod(length, k)
    result = []
    curr = head

    for i in range(k):
        dummy = ListNode(0)
        write = dummy
        for _ in range(part_size + (1 if i < remainder else 0)):
            write.next = ListNode(curr.val)
            curr = curr.next
            write = write.next
        result.append(dummy.next)

    return result
```

**Explanation:** Distribute nodes as evenly as possible among parts, some parts may be 1 node larger.

---

### **10. Sort Linked List (Merge Sort)**

```python
def sort_list(head):
    if not head or not head.next:
        return head

    def get_middle(node):
        slow = fast = node
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next, l1 = l1, l1.next
            else:
                tail.next, l2 = l2, l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next

    mid = get_middle(head)
    right = sort_list(mid.next)
    mid.next = None
    left = sort_list(head)

    return merge(left, right)
```

**Explanation:** Use merge sort to sort the linked list in O(n log n) time and O(1) space.

---

Would you like more **linked list + DP hybrid** problems next or move to another topic?
