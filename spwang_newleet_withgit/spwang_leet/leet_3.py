class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        l = 0
        ans = 0
        dic = {}
        for i, j in enumerate(s):
            if j not in dic:
                dic[j] = i
            else:
                l = max(l, dic[j] + 1)
                dic[j] = i
            ans = max(ans, i - l + 1)
        return ans

test = Solution()
print(test.lengthOfLongestSubstring("abcabcbb"))