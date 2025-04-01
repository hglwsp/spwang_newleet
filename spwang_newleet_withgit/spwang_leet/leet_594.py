from collections import defaultdict
class Solution:
    def findLHS(self, nums) -> int:
        dic = defaultdict(int)
        for i in nums:
            dic[i]+=1
        maxres = 0
        for k,v in dic.items():
            if k+1 in dic:
                maxres = max(maxres,v+dic[k+1])
        return maxres

test = Solution()
print(test.findLHS([1,3,2,2,5,2,3,7]))