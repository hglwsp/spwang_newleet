# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        def dfs(node):
            if not node:
                return 0
            if node.left and not node.left.left and not node.left.right:
                return node.left.val + dfs(node.right)
            else:
                return dfs(node.left) + dfs(node.right)
        dfs(root)
        return dfs(root)

test = Solution()
print(test.sumOfLeftLeaves(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))))

