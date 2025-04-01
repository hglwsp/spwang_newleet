class Solution:
    def threeSum(self, nums):
        # nums.sort()
        # if len(nums) < 3:
        #     return []
        # res = []
        # for i in range(len(nums)):
        #     if nums[i] > 0:
        #         return res
        #     if i > 0 and nums[i] == nums[i - 1]:
        #         continue   # 去重
        #     l = i + 1
        #     r = len(nums) - 1
        #     while l < r:
        #         if nums[i] + nums[l] + nums[r] == 0:
        #             res.append([nums[i], nums[l], nums[r]])
        #             while l < r and nums[l] == nums[l + 1]:
        #                 l += 1
        #             while l < r and nums[r] == nums[r - 1]:
        #                 r -= 1
        #             l += 1
        #             r -= 1
        #         elif nums[i] + nums[l] + nums[r] < 0:
        #             l += 1
        #         else:
        #             r -= 1
        # return res

        nums.sort()
        if len(nums) < 3:
            return []
        res = []
        path = []
        used = [False] * len(nums)
        def backtrack(res, path, used, startindex,nums):
            if len(path[:]) == 3:
                if sum(path) == 0 and path not in res:
                    res.append(path[:])
                return
            for i in range(startindex, len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(res, path, used, i + 1, nums)
                used[i] = False
                path.pop()
        backtrack(res, path, used, 0, nums)
        return res


test = Solution()
print(test.threeSum([-1, 0, 1, 2, -1, -4]))
