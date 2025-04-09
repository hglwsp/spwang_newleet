from collections import defaultdict
class Solution:
    def subarraySum(self, nums, k: int) -> int:
        d = defaultdict(int)
        ans,prev = 0,0
        # 前缀和
        d[0]=1
        for x in nums:
            prev+=x
            ans+=d[prev-k]
            d[prev]+=1
        print(d)
        return ans



test = Solution()
print(test.subarraySum([1,1,1],2))
