class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left,right = 0,0
        while right < len(nums):
            if nums[right] == 0:
                right += 1
            else:
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
                right += 1
        return nums

test = Solution()
print(test.moveZeroes([0,1,0,3,12]))