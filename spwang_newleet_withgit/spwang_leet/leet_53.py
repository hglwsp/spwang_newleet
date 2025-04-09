class Solution:
    def maxSubArray(self, nums) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        dp = [ 0 for _ in range(n) ]
        dp[0] = nums[0]
        for i in range(1,n):
            dp[i] = max(dp[i-1]+nums[i],nums[i])
        return max(dp)

test = Solution()
print(test.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))