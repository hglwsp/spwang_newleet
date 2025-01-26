from collections import defaultdict
class Solution:
    def maxOperations(self, nums, k: int) -> int:
        ans = 0
        dic = defaultdict(int)
        for num in nums:
            if k - num in dic and dic[k-num] > 0:
                dic[k-num]-=1
                ans+=1
            else:
                dic[num]+=1
        return ans

test = Solution()
print(test.maxOperations([1,2,3,4], 5))