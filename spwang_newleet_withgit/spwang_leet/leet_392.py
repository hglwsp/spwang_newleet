class Solution:
    def isSubsequence(self, s: str, t: str):
        s_p = 0
        s_t = 0
        while s_p < len(s) and s_t < len(t):
            if s[s_p] == t[s_t]:
                s_p += 1
            s_t += 1
        return s_p == len(s)

test = Solution()
print(test.isSubsequence("abc", "ahbgdc"))