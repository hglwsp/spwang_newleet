from collections import defaultdict
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        dic = defaultdict(int)
        for i in moves:
            dic[i]+=1
        return True if dic['L']==dic['R'] and dic['U']==dic['D'] else False

test = Solution()
print(test.judgeCircle("UD"))