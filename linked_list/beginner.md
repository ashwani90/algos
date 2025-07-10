Here are **10 beginner-level linked list problems** with **Python solutions and explanations**. These problems will help you get comfortable with singly linked lists and basic operations like traversal, insertion, and reversal.

---

### **1. Reverse a Linked List**

**Problem:** Reverse a singly linked list.

**Solution:**

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev
```

**Explanation:** We keep a `prev` pointer and reverse the `.next` pointer of each node while traversing.

---

### **2. Find the Middle of the Linked List**

**Problem:** Return the middle node of the linked list. If even number of nodes, return the second one.

```python
def middle_node(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```

**Explanation:** Fast moves two steps, slow moves one. When fast reaches the end, slow is in the middle.

---

### **3. Detect Cycle in a Linked List**

```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

**Explanation:** If there's a cycle, fast and slow will eventually meet.

---

### **4. Merge Two Sorted Linked Lists**

```python
def merge_two_lists(l1, l2):
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
```

**Explanation:** Use a dummy node to simplify merging sorted nodes.

---

### **5. Remove Duplicates from Sorted Linked List**

```python
def delete_duplicates(head):
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head
```

**Explanation:** If current node equals next, skip the duplicate node.

---

### **6. Delete a Node (Given Access to the Node Only)**

**Problem:** Delete a node (not tail) in a singly linked list, given only that node.

```python
def delete_node(node):
    node.val = node.next.val
    node.next = node.next.next
```

**Explanation:** Overwrite this node with the next node’s data and skip the next node.

---

### **7. Convert List to Linked List**

```python
def list_to_linked(lst):
    dummy = ListNode()
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next
```

**Explanation:** Simple utility to turn a Python list into a linked list.

---

### **8. Convert Linked List to List**

```python
def linked_to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res
```

**Explanation:** Utility to help visualize linked lists as regular Python lists.

---

### **9. Length of Linked List**

```python
def length_of_list(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count
```

**Explanation:** Traverse the list while counting nodes.

---

### **10. Sum of Two Linked Lists (Reversed Order)**

**Problem:** Each node contains a digit. The digits are stored in reverse order. Add two such lists.

```python
def add_two_numbers(l1, l2):
    dummy = ListNode()
    curr = dummy
    carry = 0
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        total = v1 + v2 + carry
        carry = total // 10
        curr.next = ListNode(total % 10)
        curr = curr.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy.next
```

**Explanation:** Like adding numbers column-wise, carry over any value > 9.

---

Would you like 10 **intermediate-level** linked list problems next (like reversing part of a list, detecting intersection, etc.)?
