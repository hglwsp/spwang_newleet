class Solution:
    def combine(self, n: int, k: int):
        res = []
        path = []
        used = [False] * (n + 1)
        startindex = 1
        def backtrack(n,k,used,path,startindex):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(startindex,n+1):
                path.append(i)
                used[i] = True
                backtrack(n,k,used,path,i+1)
                used[i] = False
                path.pop()
        backtrack(n,k,used,path,startindex)
        return res

test = Solution()
print(test.combine(4,2))