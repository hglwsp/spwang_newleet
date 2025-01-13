from collections import defaultdict
class Solution:
    def singleNumber(self, nums) -> int:
        dict = defaultdict(int)
        for i in nums:
            dict[i]+=1
        for k,v in dict.items():
            if v==1:
                return k

test = Solution()
print(test.singleNumber([2,2,1]))
