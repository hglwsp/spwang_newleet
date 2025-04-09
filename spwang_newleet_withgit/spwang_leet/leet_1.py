from collections import defaultdict
class Solution:
    def twoSum(self, nums, target):
        res = []
        d = defaultdict(int)
        for i in range(len(nums)):
            if target - nums[i] in d:
                # res.append(nums.index(x),nums.index(target - x))
                res.append(i)
                res.append(d[target - nums[i]])
                # return res
            else:
                d[nums[i]] = i
        sorted(d.items(), key=lambda x: x[1])
        print(d)



test = Solution()
print(test.twoSum([2, 7, 11, 15], 9))
