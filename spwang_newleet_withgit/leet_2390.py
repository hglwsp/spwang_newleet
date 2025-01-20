class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c == '*':
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)


if __name__ == '__main__':
    s = Solution()
    print(s.removeStars("leet**cod*e"))