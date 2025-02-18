class Solution:
    def permuteUnique(self, nums):
        res = []
        path = []
        used = [False for _ in range(len(nums))]
        def backtrack(nums, used, path):
            if len(path) == len(nums) and path not in res:
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(nums, used, path)
                used[i] = False
                path.pop()
        backtrack(nums, used, path)
        return res

test = Solution()
print(test.permuteUnique([1,1,2]))