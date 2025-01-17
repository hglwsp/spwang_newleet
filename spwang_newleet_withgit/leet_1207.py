from collections import defaultdict

class Solution:
    def uniqueOccurrences(self, arr):
        dic = defaultdict(int)
        res = []
        for i in range(len(arr)):
            dic[arr[i]] += 1
        for k,v in dic.items():
            res.append(v)
        result = list(set(res))
        return len(res) == len(result)

test = Solution()
print(test.uniqueOccurrences([1,2,2,1,1,3,3]))