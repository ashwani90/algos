'''
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation 
sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a 
list of the words [beginWord, s1, s2, ..., sk].

'''

from collections import defaultdict, deque
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        if endWord not in word_set:
            return []

        L = len(beginWord)
        alps = 'abcdefghijklmnopqrstuvwxyz'

        # parents[child] = set of words from previous layer that lead to child
        parents = defaultdict(set)

        # current layer (set of words)
        layer = {beginWord}

        # BFS layer-by-layer building parents until endWord appears
        while layer and endWord not in parents:
            # remove the current layer words from word_set so next layer can't reuse them
            word_set -= layer
            next_layer = set()

            for word in layer:
                for i in range(L):
                    base = word[:i] + word[i+1:]
                    for c in alps:
                        if c == word[i]:
                            continue
                        nei = base[:i] + c + base[i:] if False else word[:i] + c + word[i+1:]
                        # simpler: nei = word[:i] + c + word[i+1:]
                        nei = word[:i] + c + word[i+1:]
                        if nei in word_set:
                            parents[nei].add(word)
                            next_layer.add(nei)

            layer = next_layer

        # if endWord not reached
        if endWord not in parents:
            return []

        # backtrack from endWord to beginWord using parents graph
        res = []
        path = [endWord]

        def dfs(word):
            if word == beginWord:
                # path currently from endWord -> ... -> beginWord, so reverse
                res.append(path[::-1].copy())
                return
            for p in parents[word]:
                path.append(p)
                dfs(p)
                path.pop()

        dfs(endWord)
        return res
