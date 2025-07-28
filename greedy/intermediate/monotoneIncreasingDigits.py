"""
Montone increasing digits

"""

def increasingDigits(n):
    digits = list(str(n))
    mark = len(n)
    for i in range(len(digits)):
        if digits[i] < digits[i-1]:
            mark = i
            digits[i-1] = str(int(digits[i-1])+1)
    
    for i in range(mark, len(digits)):
        digits[i] = '9'
    
    return int(''.join(digits))