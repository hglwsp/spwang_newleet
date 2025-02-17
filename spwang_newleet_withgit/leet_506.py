from collections import defaultdict
class Solution:
    def findRelativeRanks(self, score):
        dic = defaultdict(str)
        scores = sorted(score, reverse=True)
        for i in range(len(scores)):
            if i == 0:
                dic[scores[i]] = "Gold Medal"
            elif i == 1:
                dic[scores[i]] = "Silver Medal"
            elif i == 2:
                dic[scores[i]] = "Bronze Medal"
            else:
                dic[scores[i]] = str(i+1)
        return [dic[i] for i in score]

test = Solution()
print(test.findRelativeRanks([5,4,3,2,1]))