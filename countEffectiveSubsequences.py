from itertools import accumulate
from functools import reduce
from operator import or_

MOD = 10**9 + 7

pw = list(
    accumulate(
        range(10**5),
        func=lambda a,_:(a<<1)%MOD,
        initial=1
    )
)

ppc = list(
    map(
        int.bit_count,
        range(1<<20)
    )
)

class Solution:

    def countEffective(
        self,
        nums
    ):

        M = reduce(or_, nums)

        bl = M.bit_length()

        bit = 1 << bl

        n = len(nums)

        cnt = [0]*bit

        for x in nums:
            cnt[x]+=1

        # SOS DP
        for k in range(bl):

            b = bb = 1<<k

            while b < bit:

                cnt[b] += cnt[
                    b^bb
                ]

                b = (
                    b+1
                )|bb

        ans = 0

        sub = M

        while True:

            term = pw[
                cnt[sub]
            ]

            if ppc[
                M^sub
            ]&1:

                ans -= term

            else:

                ans += term

            if sub==0:
                break

            sub = (
                sub-1
            )&M

        return (
            pw[n]-ans
        )%MOD