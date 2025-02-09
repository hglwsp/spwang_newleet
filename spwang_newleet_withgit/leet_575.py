class Solution:
    def distributeCandies(self, candyType):
        return len(list(set(candyType))) if len(list(set(candyType))) < len(candyType) // 2 else len(candyType) // 2

test = Solution()
print(test.distributeCandies([1,1,2,2,3,3]))