class Solution:
    def trailingZeroes(self, n):
        k5 = 0
        for i in range(1,n+1):
            while i%5 == 0:
                k5+=1
                i = i/5
        return k5

test = Solution()
print(test.trailingZeroes(n = 30))