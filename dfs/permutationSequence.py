class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = []
        used = [False]*n
        val = None
        found = False
        def dfs(cur):
            nonlocal found
            nonlocal val
            if len(cur) == n:
                ct = cur[:]
                res.append("".join(ct))
                if len(res) == k:
                    found = True
                    val = res[-1]
                return 
            if found:
                return
            for i in range(n):
                if used[i]:
                    continue
                
                cur.append(str(i+1))
                used[i] = True
                dfs(cur)
                cur.pop()
                used[i] = False
        dfs([])
        return val