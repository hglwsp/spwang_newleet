class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        return S[:length].replace(' ', '%20')

test = Solution()
print(test.replaceSpaces("Mr John Smith    ", 13))