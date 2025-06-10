"""

Word break 2 problem

s string and dictionaru of words, return all possible sentences where s can be segmented into dict words

"""

def word_break(s, wordDict):
    memo = {}
    def backtrack(start):
        if start == len(s):
            return [""]
        
        if start in memo:
            return memo[start]
        
        res = []
        for end in range(start+1, len(s)+1):
            word = s[start:end]
            if word in wordDict:
                for sub in backtrack(end):
                    sentence = word + (" " + sub if sub else "")
                    res.append(sentence)
        
        memo[start] = res
        return res
    
    return backtrack(0)