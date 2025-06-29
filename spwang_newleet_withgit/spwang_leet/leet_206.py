class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        if not head or not head.next:
            return head
        cur,pre = head,None
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

test = Solution()
print(test.reverseList(ListNode(1,ListNode(2,ListNode(2,ListNode(1))))))