class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:] # [2:] to remove the '0b'


test = Solution()
print(test.addBinary("11", "1"))