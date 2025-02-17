class Solution:
    def sortArrayByParityII(self, nums):
        nums1 = []
        nums2 = []
        for i in nums:
            if i % 2 == 0:
                nums1.append(i)
            else:
                nums2.append(i)
        res = []
        for j in range(len(nums1)):
            res.append(nums1[j])
            res.append(nums2[j])
        return res

test= Solution()
print(test.sortArrayByParityII([4,2,5,7]))