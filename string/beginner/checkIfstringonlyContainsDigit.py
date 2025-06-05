"""

Check if string only contains digit

"""

def containsOnlyDigit(s):
    all_digits = "0123456789"
    for i in s:
        if i not in all_digits:
            return False
    
    return True
