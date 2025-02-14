from collections import defaultdict
class Solution:
    def sumOfUnique(self, nums) -> int:
        dic = defaultdict(int)
        for i in nums:
            dic[i] += 1
        res = 0
        for k,v in dic.items():
            if v == 1:
                res += k
        return res

test = Solution()
print(test.sumOfUnique([1,2,3,2]))