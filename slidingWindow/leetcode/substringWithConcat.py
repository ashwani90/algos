"""
You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

"""

def substringWithConcat(s, words):
    if not s or not words:
        return []
    word_len = len(words[0])
    num_words = len(words)
    total_len = word_len * num_words
    word_count = Counter(words)

    result = []

    for i in range(word_len):
        left = i
        right = i 
        current_count = Counter()
        while right + word_len <= len(s):
            word = s[right:right+word_len]
            right += word_len

            if word in word_count:
                current_count[word] += 1
                while current_count[word] > word_count[word]:
                    left_word = s[left:left+word_len]
                    current_count[left_word] -= 1
                    left += word_len
                if right-left == total_len:
                    result.append(left)
            else:
                current_count.clear()
                left=right
    
    return result