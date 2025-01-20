class Solution:
    def findClosestNumber(self, nums):
        nums.sort()
        flag = float('inf')
        res = nums[0]
        for i in range(len(nums)):
            if abs(nums[i]) <= flag:
                res = nums[i]
                flag = abs(nums[i])
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.findClosestNumber([-4,-2,1,4,8]))
