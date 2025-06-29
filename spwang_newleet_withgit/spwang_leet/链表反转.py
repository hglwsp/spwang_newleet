# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur, pre = head, None
        while cur:
            tmp = cur.next  # 暂存后继节点 cur.next
            cur.next = pre  # 修改 next 引用指向
            pre = cur  # pre 暂存 cur
            cur = tmp  # cur 访问下一节点
        return pre

