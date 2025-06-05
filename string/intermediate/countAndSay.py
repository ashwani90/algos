"""

Count and say 
given an interegr , generate nth term of count and say sequence

"""

def countAndSay(n):
    if n == 1:
        return "1"
    
    prev = countAndSay(n-1)
    result = ""
    count = 1

    for i in range(1, len(prev)+1):
        if i < len(prev) and prev[i] == prev[i-1]:
            count += 1
        else:
            result += str(count) + prev[i-1]
            count = 1
    
    return result