class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []
        path = []
        used = [False] * len(digits)
        startindex = 0
        def backtrack(digits, path, used,startindex):
            if len(path) == len(digits):
                res.append("".join(path))
                return
            for i in range(startindex,len(digits)):
                if used[i]:
                    continue
                for j in range(len(phoneMap[digits[i]])):
                    path.append(phoneMap[digits[i]][j])
                    used[i] = True
                    backtrack(digits, path, used,startindex+1)
                    used[i] = False
                    path.pop()
        backtrack(digits, path, used,startindex)
        return res



test = Solution()
print(test.letterCombinations("23"))
