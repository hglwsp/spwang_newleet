class Solution:
    def canPlaceFlowers(self, flowerbed, n: int):
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
        return n <= 0

test = Solution()
print(test.canPlaceFlowers([1,0,0,0,1], 1))