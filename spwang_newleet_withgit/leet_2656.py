class Solution:
    def maximizeSum(self, nums, k: int) -> int:
        nums.sort()
        return  k*nums[-1] + k*(k-1)//2

test = Solution()
print(test.maximizeSum([1,2,3,4,5], 3))