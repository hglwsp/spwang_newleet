from collections import defaultdict
class Solution:
    def getSneakyNumbers(self, nums):
        dic = defaultdict(int)
        for i in nums:
            dic[i] += 1
        res = []
        for k,v in dic.items():
            if v == 2:
                res.append(k)
            if len(res) == 2:
                return res

test = Solution()
print(test.getSneakyNumbers([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]))