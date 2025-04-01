class Solution:
    def pivotIndex(self, nums) -> int:
        left = 0
        right = sum(nums)
        for i in range(len(nums)):
            right -= nums[i]
            if left == right:
                return i
            left += nums[i]
        return -1

test = Solution()
print(test.pivotIndex([1,7,3,6,5,6]))
