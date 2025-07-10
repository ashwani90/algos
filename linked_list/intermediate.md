Here are **10 intermediate-level linked list problems** with **Python solutions and detailed explanations**. These problems cover a variety of concepts such as sublist reversal, cycle detection, intersection, and more.

---

### **1. Reverse a Sublist (Between Left and Right)**

**Problem:** Given a linked list, reverse the nodes from position `left` to `right`.

```python
def reverse_between(head, left, right):
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    for _ in range(left - 1):
        prev = prev.next

    curr = prev.next
    for _ in range(right - left):
        temp = curr.next
        curr.next = temp.next
        temp.next = prev.next
        prev.next = temp

    return dummy.next
```

**Explanation:** Reverse the sublist using in-place reversal. We move the next node in front iteratively.

---

### **2. Remove N-th Node from End of List**

```python
def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)
    slow = fast = dummy

    for _ in range(n + 1):
        fast = fast.next

    while fast:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return dummy.next
```

**Explanation:** Use two pointers. `fast` is ahead by `n` steps, so when it reaches end, `slow` is before node to remove.

---

### **3. Detect and Return Start of Cycle**

```python
def detect_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow == fast:
            break
    else:
        return None

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow
```

**Explanation:** First detect the cycle using Floyd’s algorithm, then reset one pointer to head and move both until they meet again.

---

### **4. Check if a Linked List is Palindrome**

```python
def is_palindrome(head):
    slow = fast = head
    stack = []

    while fast and fast.next:
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next.next

    if fast:  # odd length, skip middle
        slow = slow.next

    while slow:
        if stack.pop() != slow.val:
            return False
        slow = slow.next
    return True
```

**Explanation:** Use a stack to store first half, then compare with second half.

---

### **5. Rotate Linked List Right by K Places**

```python
def rotate_right(head, k):
    if not head:
        return None

    # Count length
    old_tail = head
    length = 1
    while old_tail.next:
        old_tail = old_tail.next
        length += 1

    k = k % length
    if k == 0:
        return head

    # Make it circular and break at new head
    old_tail.next = head
    new_tail = head
    for _ in range(length - k - 1):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None
    return new_head
```

**Explanation:** Connect tail to head, then break the circle at `(length - k)`.

---

### **6. Merge K Sorted Linked Lists**

```python
import heapq

def merge_k_lists(lists):
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))

    dummy = ListNode()
    curr = dummy
    while heap:
        _, i, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next
```

**Explanation:** Use a min-heap to always pull the smallest head node from all lists.

---

### **7. Partition List Around a Value**

```python
def partition(head, x):
    before = before_head = ListNode()
    after = after_head = ListNode()

    while head:
        if head.val < x:
            before.next = head
            before = before.next
        else:
            after.next = head
            after = after.next
        head = head.next

    after.next = None
    before.next = after_head.next
    return before_head.next
```

**Explanation:** Split into two lists based on `x`, then combine them.

---

### **8. Find Intersection Node of Two Lists**

```python
def get_intersection_node(headA, headB):
    a, b = headA, headB
    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a
```

**Explanation:** Switch lists at the end. They'll align at intersection or None.

---

### **9. Swap Nodes in Pairs**

```python
def swap_pairs(head):
    dummy = ListNode(0)
    dummy.next = head
    curr = dummy

    while curr.next and curr.next.next:
        first = curr.next
        second = curr.next.next

        first.next = second.next
        second.next = first
        curr.next = second

        curr = first
    return dummy.next
```

**Explanation:** Swap every two nodes using pointer adjustments.

---

### **10. Odd Even Linked List**

**Problem:** Group all odd-indexed nodes followed by even-indexed nodes.

```python
def odd_even_list(head):
    if not head or not head.next:
        return head

    odd = head
    even = head.next
    even_head = even

    while even and even.next:
        odd.next = even.next
        odd = odd.next

        even.next = odd.next
        even = even.next

    odd.next = even_head
    return head
```

**Explanation:** Use two pointers to segregate odd and even indexed nodes, then join them.

---

Would you like to proceed to **advanced-level linked list problems** next?
