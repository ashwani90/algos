class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        used = [False] * n
        dcheck = {}

        def dfs(cur):
            if len(cur) == n:
                if str(cur) not in dcheck:
                    dcheck[str(cur)] = True
                    res.append(cur[:])
                return 
                
            for i in range(n):
                if used[i]:
                    continue
                cur.append(nums[i])
                used[i] = True
                dfs(cur)
                cur.pop()
                used[i] = False
        dfs([])
        return res
                
                