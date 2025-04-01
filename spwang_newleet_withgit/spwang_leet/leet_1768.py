class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = min(len(word1), len(word2))
        ans = ""
        flag = 0
        while min_len > 0:
            ans+=word1[flag]
            ans+=word2[flag]
            flag+=1
            min_len-=1
        if flag < len(word1):
            ans+=word1[flag:]
        if flag < len(word2):
            ans+=word2[flag:]
        return ans

test = Solution()
print(test.mergeAlternately("abc", "pqr"))