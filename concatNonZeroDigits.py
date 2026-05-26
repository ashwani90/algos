class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        s = ''
        st = 0
        for i in str(n):
            if i != '0':
                s += str(i)
                st += int(i)
            
        return st * int(s)