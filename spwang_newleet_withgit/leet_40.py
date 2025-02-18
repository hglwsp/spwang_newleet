class Solution:
    def combinationSum2(self, candidates, target: int):
        candidates.sort()
        res = []
        path = []
        startindex = 0
        used = [False for _ in range(len(candidates))]

        def backtrack(candidates, target, startindex, path, res,used):
            if sum(path) == target and path not in res:
                res.append(path[:])
                return
            if sum(path) > target:
                return
            for i in range(startindex, len(candidates)):
                if used[i]:
                    continue
                if candidates[i] > target:
                    break
                if i > startindex and candidates[i] == candidates[i-1]:
                    continue
                used[i] = True
                path.append(candidates[i])
                backtrack(candidates, target, i+1, path, res,used)
                used[i] = False
                path.pop()

        backtrack(candidates, target, startindex, path, res,used)
        return res

test = Solution()
print(test.combinationSum2([10,1,2,7,6,1,5], 8))