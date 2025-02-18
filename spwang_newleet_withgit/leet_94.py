class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root):
        # res = []
        # if root:
        #     res += self.inorderTraversal(root.left)
        #     res.append(root.val)
        #     res += self.inorderTraversal(root.right)
        # return res
        res = []
        def zs(root):
            if not root:
                return []
            zs(root.left)
            res.append(root.val)
            zs(root.right)
            return res

test = Solution()
print(test.inorderTraversal(TreeNode(1,None,TreeNode(2,TreeNode(3)))))