'''

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

'''

def longestCommonPrefix(strs):
    min_length = float("inf")
    for i in strs:
        min_length = min(min_length, len(strs))
    if min_length == 0:
        return ""

    for i in range(min_length):
        c = strs[0][i]
        for j in strs:
            if j[i] != c:
                return strs[0][:i]
            