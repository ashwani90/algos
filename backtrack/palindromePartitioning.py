"""

Palindrome partitioning 
partition a string so that the substring is a palindrome

"""

def partitionPalindrome(s):
    result = []

    def is_palindrome(s):
        return s == s[::-1]
    
    def backtrack(start, path):
        if start == len(s):
            result.append(path[:])
            return
        
        for end in range(start, len(s)+1):
            if is_palindrome(s[start:end]):
                path.append(s[start:end])
                backtrack(start,path)
                path.pop()
    
    backtrack(0, [])
    return result