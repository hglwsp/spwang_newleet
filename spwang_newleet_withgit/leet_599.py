from collections import defaultdict
class Solution:
    def findRestaurant(self, list1, list2):
        dic = defaultdict(int)
        for i in range(len(list1)):
            dic[list1[i]] = i
        res = []
        flag = float('inf')
        for i in range(len(list2)):
            if list2[i] in dic:
                if i + dic[list2[i]] < flag:
                    res = []
                    res.append(list2[i])
                    flag = i + dic[list2[i]]
                elif i + dic[list2[i]] == flag:
                    res.append(list2[i])
                    flag = i + dic[list2[i]]
        return res

test = Solution()   ###
print(test.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],["KFC","Shogun","Burger King"]))
