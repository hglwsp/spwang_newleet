class Solution:
    def increasingTriplet(self, nums) -> bool:
        # if not nums:
        #     return False
        # dp = [1] * len(nums)
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        # return max(dp) >= 3
        a = b = float('inf')
        for c in nums:
            if c <= a:
                a = c
            elif c <= b:
                b = c
            else:
                return True
        return False

test = Solution()
print(test.increasingTriplet([4,5,2147483647,1,2]))