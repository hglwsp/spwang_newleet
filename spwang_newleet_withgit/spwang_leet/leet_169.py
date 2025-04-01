from collections import defaultdict
class Solution:
    def majorityElement(self, nums):
        dic = defaultdict(int)
        for num in nums:
            dic[num]+=1
        for k,v in dic.items():
            if v > len(nums)//2:
                return k

test = Solution()
print(test.majorityElement([1,2,3,2,2,2,5,4,2]))