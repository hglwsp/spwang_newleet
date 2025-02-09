from collections import defaultdict
class Solution:
    def intersection(self, nums1, nums2):
        d_nums2 = list(set(nums2))
        dic = defaultdict(int)
        for num in nums1:
            dic[num] += 1
        res = []
        for num in d_nums2:
            if dic[num] > 0:
                res.append(num)
        return res

test = Solution()
print(test.intersection([1,2,2,1], [2,2]))
