class Solution:
    def subsetsWithDup(self, nums):
        res = []
        path = []
        used = [False for _ in range(len(nums))]
        def backtrack(nums, path, used,index):
            if path not in res:
                res.append(path[:])
            if index == len(nums):
                return
            for i in range(index, len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(nums, path, used, i+1)
                used[i] = False
                path.pop()
        backtrack(nums, path, used, 0)
        return res
test = Solution()
print(test.subsetsWithDup([1,2,2]))