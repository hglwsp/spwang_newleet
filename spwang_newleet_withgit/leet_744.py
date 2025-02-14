class Solution:
    def nextGreatestLetter(self, letters, target: str) -> str:
        for i in letters:
            if i > target:
                return i
        return letters[0]

test = Solution()
print(test.nextGreatestLetter(["c","f","j"], "a"))