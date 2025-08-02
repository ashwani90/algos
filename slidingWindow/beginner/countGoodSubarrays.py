"""
roblem: Return the count of substrings of size k that have k distinct characters.

"""

def count_good_substrings(s, k):
    count = 0
    for i in range(len(s) - k + 1):
        if len(set(s[i:i+k])) == k:
            count += 1
    return count