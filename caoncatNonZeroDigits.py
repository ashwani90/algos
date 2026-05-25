from bisect import bisect_left, bisect_right

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        digits = []
        pos = []

        for i, ch in enumerate(s):
            if ch != '0':
                digits.append(int(ch))
                pos.append(i)

        n = len(digits)

        pref = [0]*(n+1)
        digitPref = [0]*(n+1)

        pow10 = [1]*(n+1)

        for i in range(n):

            pref[i+1] = (
                pref[i]*10 + digits[i]
            ) % MOD

            digitPref[i+1] = digitPref[i] + digits[i]

            pow10[i+1] = (
                pow10[i]*10
            ) % MOD

        ans = []

        for l,r in queries:

            L = bisect_left(pos,l)
            R = bisect_right(pos,r)-1

            if L > R:
                ans.append(0)
                continue

            length = R-L+1

            x = (
                pref[R+1]
                - pref[L]*pow10[length]
            ) % MOD

            sm = (
                digitPref[R+1]
                - digitPref[L]
            )

            ans.append((x*sm)%MOD)

        return ans
