class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def level_order_list_to_bst(level_order_list):
        if not level_order_list:
            return None

        from collections import deque

        root = TreeNode(level_order_list[0])
        queue = deque([root])
        i = 1  # 从列表的第二个元素开始，因为第一个元素已经是根节点了

        while queue and i < len(level_order_list):
            current_node = queue.popleft()

            # 检查左子节点是否存在
            if i < len(level_order_list) and level_order_list[i] is not None:  # 注意这里假设None表示空位
                current_node.left = TreeNode(level_order_list[i])
                queue.append(current_node.left)

            # 检查右子节点是否存在（注意i已经自增了，所以这里是i而不是i+1）
            i += 1
            if i < len(level_order_list) and level_order_list[i] is not None:
                current_node.right = TreeNode(level_order_list[i])
                queue.append(current_node.right)

            i += 1  # 移动到下一个潜在节点的位置（无论是左子节点还是右子节点之后）
        print(queue)
        return root
    def getMinimumDifference(self, root) -> int:
        res = []
        def zs(root):
            if not root:
                return
            zs(root.left)
            res.append(root.val)
            zs(root.right)
        zs(root)
        ans = float('inf')
        for i in range(len(res)-1):
            ans = min(ans,res[i+1]-res[i])
        return ans

test = Solution()
need_root = [1,0,48,None,None,12,49]
root = Solution.level_order_list_to_bst(need_root)
print(root)
print(test.getMinimumDifference(root))