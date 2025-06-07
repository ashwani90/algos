"""

Decode string 3[a]2[bc]
decode it to aaabcbc
"""

def decodeString(s):
    stack = []
    current_num = 0
    current_string = ""

    for char in s:
        if char.isdigit():
            current_num = current_num*10+char
        elif char == '[':
            stack.append((current_num, current_string))
            current_string = ""
            current_num = 0
        elif char == ']':
            prev_num, prev_string = stack.pop()
            current_string = prev_string + current_string*prev_num # this is the most complicated part for this
        else:
            current_string += char
        
    
    return current_string