from collections import defaultdict
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dic = defaultdict(int)
        for i in text:
            dic[i] += 1
        minres = float('inf')
        flag = 0
        for k,v in dic.items():
            if k in ['b','a','l','o','n']:
                flag+=1
                if k == "l" or k == "o":
                    if v < 2:
                        return 0
                    else:
                        minres = min(minres,v//2)
                else:
                    minres = min(minres,v)
        return minres if flag == 5 else 0

test = Solution()
print(test.maxNumberOfBalloons("loonbalxballpoon"))
