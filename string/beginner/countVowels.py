"""

Count vowels in a string

"""

def countVowels(s):
    vowels = "aeiouAEIOU"
    count = 0

    for i in s:
        if i in vowels:
            count += 1
    
    return vowels