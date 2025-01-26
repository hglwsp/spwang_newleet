class Solution:
    def largestAltitude(self, gain) -> int:
        new_gain = [0] + gain
        res = [0] * len(new_gain)
        for i in range(1, len(new_gain)):
            res[i] = res[i - 1] + new_gain[i]
        return max(res)

test = Solution()
print(test.largestAltitude([-5,1,5,0,-7]))