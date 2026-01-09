"""
You are given an integer n representing the length of an unknown array that you are trying to recover. You are also given an array sums containing the values of all 2n subset sums of the unknown array (in no particular order).

Return the array ans of length n representing the unknown array. If multiple answers exist, return any of them.

An array sub is a subset of an array arr if sub can be obtained from arr by deleting some (possibly zero or all) elements of arr. The sum of the elements in sub is one possible subset sum of arr. The sum of an empty array is considered to be 0.

Note: Test cases are generated such that there will always be at least one correct answer.


"""

class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        # Sort the subset sums
        sums.sort()
        result = []

        # recover one element at a time
        for _ in range(n):
            # The smallest element is always 0 (empty subset)
            # The second smallest is the next element difference
            x = sums[1] - sums[0]

            # Counter to manage multiset
            count = Counter(sums)

            # Two groups:
            # group_without_x: subset sums NOT having x
            # group_with_x: subset sums having x
            group_without_x = []
            group_with_x = []

            # divide sums into two groups
            for s in sums:
                if count[s] == 0:
                    continue

                # s belongs to group_without_x
                group_without_x.append(s)
                count[s] -= 1

                # s + x must exist in the multiset
                count[s + x] -= 1
                group_with_x.append(s + x)

            # Decide whether x is positive or negative
            # The empty subset (0) must be in group_without_x
            if 0 in group_without_x:
                # x is positive
                result.append(x)
                sums = group_without_x
            else:
                # x is negative
                result.append(-x)
                sums = group_with_x

            # Prepare for next iteration
            sums.sort()

        return result