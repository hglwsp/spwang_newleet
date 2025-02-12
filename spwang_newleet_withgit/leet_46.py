class Solution:
    def permute(self, nums):
        # 回溯法模板
        # 选择，递归，撤销选择
        # n = len(nums)
        # res = []
        # path = []
        # used = [False]*n
        # def backtrack(nums,path,used):
        #     # 判断是否触发结束条件
        #     if len(path) == n:
        #         res.append(path[:])
        #         return
        #     else:
        #         for i in range(n):
        #             if used[i]:   # nums[i]选过，跳过
        #                 continue
        #             # 选择回溯递归
        #             path.append(nums[i])
        #             used[i] = True
        #             backtrack(nums,path,used)
        #             # 撤销选择
        #             path.pop()
        #             used[i] = False
        # backtrack(nums,path,used)
        # return res

        res = []
        path = []
        used = [False]*len(nums)
        def backtrack(nums,path,used):
            if len(path[:]) == len(nums):
                res.append(path[:])
                return
            else:
                for i in range(len(nums)):
                    if used[i]:
                        continue
                    path.append(nums[i])
                    used[i] = True
                    backtrack(nums,path,used)
                    path.pop()
                    used[i] = False
        backtrack(nums,path,used)
        return res

test = Solution()
print(test.permute([1,2,3]))