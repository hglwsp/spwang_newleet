class Solution:
    def subsetsWithDup(self, nums):
        res = []
        path = []
        used = [False] * len(nums)
        def backtrack(nums, used, path,index):
            if path[:] not in res:
                res.append(path[:])
            if index == len(nums):
                return
            for i in range(index, len(nums)):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = True
                backtrack(nums, used, path, i + 1)
                used[i] = False
                path.pop()
        backtrack(nums, used, path, 0)
        return res

test = Solution()
print(test.subsetsWithDup([1,2,2]))