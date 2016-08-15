# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        # split into two
        if not head or not head.next:
            return
        ph = pre = ListNode(0)
        pre.next = head
        slow = fast = ph
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        ph.next, slow.next = slow.next, None
        # reverse the second half
        pre, ps = ph, ph.next
        while ps.next:
            p = ps.next
            ps.next = p.next
            p.next = pre.next
            pre.next = p
        # splice them together
        cur1, cur2 = head, ph.next
        pre = ph
        while cur1 or cur2:
            if cur1:
                pre.next, cur1 = cur1, cur1.next
                pre = pre.next
            if cur2:
                pre.next, cur2 = cur2, cur2.next
                pre = pre.next
