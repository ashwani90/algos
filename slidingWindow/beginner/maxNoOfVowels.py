"""

Problem: Given a string and an integer k, return the maximum number of vowels in any substring of length k.
It is just a moving window problem
Move window from start to end

"""

def max_vowels(s, k):
    vowels = set('aeiou')
    count = sum(1 for c in s[:k] if c in vowels)
    max_count = count

    for i in range(k, len(s)):
        if s[i-k] in vowels:
            count -= 1
        if s[i] in vowels:
            count += 1
        max_count = max(max_count, count)
    return max_count
