class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        total = sum(nums[:k])
        res = total / k
        for i in range(k, len(nums)):
            total += nums[i] - nums[i - k]
            res = max(res,total/k)
        return res

test = Solution()
print(test.findMaxAverage([1,12,-5,-6,50,3], 4))