class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        def solve(nums):
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, n-1):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            return dp[-1]
        res = max(solve(nums[:-1]), solve(nums[1:]))
        return res

test = Solution()
print(test.rob([1,2,1,1]))
print(test.rob([2,3,2]))
