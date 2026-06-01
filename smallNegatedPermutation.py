class Solution:
    def lexSmallestNegatedPerm(self, n: int, target: int) -> List[int]:
        S = n * (n + 1) // 2

        if target < -S or target > S:
            return []

        D = S - target

        if D % 2:
            return []

        ans = [i for i in range(1, n + 1)]

        for x in range(n, 0, -1):

            if 2 * x <= D:
                ans[x - 1] = -x
                D -= 2 * x

        if D != 0:
            return []

        ans.sort()

        return ans