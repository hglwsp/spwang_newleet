class Solution:
    def findDuplicate(self, nums):
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return fast

test = Solution()
print(test.findDuplicate([1,3,4,2,2]))