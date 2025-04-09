class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        p0,p2 = 0,n-1
        i = 0
        while i <= p2:
            if nums[i] == 0:
                nums[i],nums[p0] = nums[p0],nums[i]
                p0 += 1
                i+=1
            elif nums[i] == 2:
                nums[i],nums[p2] = nums[p2],nums[i]
                p2-=1
            else:
                i+=1
        return nums

test = Solution()
print(test.sortColors([2,0,2,1,1,0]))