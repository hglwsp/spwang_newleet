# leet_144.py
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

# 创建 l_t_t 类的实例
converter = l_t_t()

# 定义层序遍历列表
need_root = [1, 0, 48, None, None, 12, 49]

# 使用 level_order_list_to_bst 方法创建二叉树
tree = converter.list_to_tree(need_root)

# 前序遍历
test = Solution()
print(test.preorder_traversal(tree))  # 输出: [1, 0, 48, 12, 49]
