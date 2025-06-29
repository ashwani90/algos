"""

Word ladder problem

Given beginWord, endWord, and a word list, find shortest transformation from begin to end, changing one letter at a time, and all intermediate words in word list.
"""

from collections import deque

def word_ladder(beginWord, endWord, wordList):
    word_set = set(wordList)
    if endWord not in word_set:
        return 0
    
    queue = deque([(beginWord, 1)])
    while queue:
        word,length = queue.popleft()
        if word == endWord:
            return length
        
        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                next_word = word[:i] + c + word[i:]
                if next_word in word_set:
                    word_set.remove(next_word)
                    queue.append((next_word, length+1))
    
    return 0