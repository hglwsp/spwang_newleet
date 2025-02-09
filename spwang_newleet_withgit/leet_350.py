from collections import defaultdict

class Solution:
    def intersect(self, nums1, nums2):
        dic = defaultdict(int)
        for num in nums1:
            dic[num] += 1
        res = []
        for num in nums2:
            if dic[num] > 0:
                dic[num] -= 1
                res.append(num)
        return res

test = Solution()
print(test.intersect([1,2,2,1], [2,2]))