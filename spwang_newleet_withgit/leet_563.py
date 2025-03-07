# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTilt(self, root):
        def search(root):
            if not root:
                return 0,0
            l_sum,l_diff = search(root.left)
            r_sum,r_diff = search(root.right)
            return root.val + l_sum + r_sum, abs(l_sum - r_sum) + l_diff + r_diff

        return search(root)[1]

test = Solution()
print(test.findTilt(TreeNode(1,TreeNode(2),TreeNode(3))))