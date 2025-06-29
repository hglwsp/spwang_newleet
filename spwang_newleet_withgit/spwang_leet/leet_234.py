class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        if not head or not head.next:
            return True
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # res = []
        # while head:
        #     res.append(head.val)
        #     head = head.next
        # if res == res[::-1]:
        #     return True
        # else:
        #     return False
        def reverse(node):
            cur, pre = node, None
            while cur:
                temp = cur.next
                cur.next = pre
                pre = cur
                cur = temp
            return pre

        last = reverse(slow)
        first = head
        while last:
            if last.val != first.val:
                return False
            last = last.next
            first = first.next
        return True

test = Solution()
print(test.isPalindrome(ListNode(1,ListNode(2,ListNode(2,ListNode(1))))))