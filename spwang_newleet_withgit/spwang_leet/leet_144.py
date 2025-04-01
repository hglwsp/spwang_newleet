from list_to_tree import l_t_t
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def preorder_traversal(self,root):
        res = []
        def dfs(node):
            if node:
                res.append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return res

# 转换列表为二叉树
converter = l_t_t()
need_root = [1, 0, 48, None, None, 12, 49]
tree = converter.list_to_tree(need_root)

# 创建 Solution 类的实例
test = Solution()

# 前序遍历
print(test.preorder_traversal(tree))  # 输出: [1, 0, 48, 12, 49]