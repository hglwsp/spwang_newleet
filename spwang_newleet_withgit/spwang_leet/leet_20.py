class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack = []
        for i in s:
            if i in dic:
                stack.append(i)
            else:
                if len(stack) == 0 or dic[stack[-1]]!=i:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0


        # dic = {
        #     '(': ')',
        #     '[': ']',
        #     '{': '}'
        # }
        # stack = []
        # for i in s:
        #     if i in dic:
        #         stack.append(i)
        #     else:
        #         if len(stack) == 0 or dic[stack[-1]]!=i:
        #             return False
        #         else:
        #             stack.pop()
        # return len(stack) == 0


test = Solution()
print(test.isValid("))"))