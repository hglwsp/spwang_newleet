class Solution:
    def minOperations(self, nums, k: int) -> int:
        res = 0
        nums.sort()
        for i in range(len(nums)):
            if nums[i] < k:
                res+=1
            else:
                return res
        return res

test = Solution()
print(test.minOperations([1,5,2,1,9,2,1,7,2,1], 5))