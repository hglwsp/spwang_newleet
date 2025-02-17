from collections import defaultdict
class Solution:
    def findSpecialInteger(self, arr):
        dic = defaultdict(int)
        for i in arr:
            dic[i] += 1
        for k,v in dic.items():
            if v > len(arr) / 4:
                return k

test = Solution()
print(test.findSpecialInteger([1,2,2,6,6,6,6,7,10]))