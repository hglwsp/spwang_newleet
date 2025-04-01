class Solution:
    def combinationSum(self, candidates, target: int):
        res = []
        path = []
        startindex = 0
        def backtrack(candidates, target, startindex, path, res):
            if target < 0:
                return
            if sum(path) == target:
                res.append(path[:])
                return
            if sum(path) > target:
                return
            for i in range(startindex, len(candidates)):
                path.append(candidates[i])
                backtrack(candidates, target, i, path, res)
                path.pop()
        backtrack(candidates, target, startindex, path, res)
        return res

test = Solution()
print(test.combinationSum([2,3,6,7], 7))
