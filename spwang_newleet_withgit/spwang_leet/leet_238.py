class Solution:
    def productExceptSelf(self, nums):
        ans,tmp = [1]*len(nums),1
        for i in range(1,len(nums)):
            ans[i] = ans[i-1]*nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            tmp *= nums[i+1]
            ans[i] *= tmp
        return ans

test = Solution()
print(test.productExceptSelf([1,2,3,4]))