"""

Remove Duplicate Letters (Lexicographically Smallest)

# Remove duplicates so the result is the smallest in lexicographical order and each letter appears once.


"""

def remove_dups(s):
    last = {c:i for i, c in enumerate(s)}

    stack = []
    seen = set()
    for i, c in enumerate(s):
        while stack and c < stack[-1] and i < last[stack[-1]]:
            seen.remove(stack.pop())

        stack.append(c)
        seen.add(c)

    return ''.join(stack)