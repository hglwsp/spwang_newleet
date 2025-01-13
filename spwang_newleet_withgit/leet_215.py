class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]

test = Solution()
print(test.findKthLargest([3,2,1,5,6,4], 2))