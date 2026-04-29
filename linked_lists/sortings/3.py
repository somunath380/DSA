# https://leetcode.com/problems/sort-list/description/
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def get_middle_node(self, head: ListNode):
        slow, fast = head, head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return head, mid
    def merge_lists(self, left: ListNode, right: ListNode):
        res = temp = ListNode()
        l1, l2 = left, right
        while l1 and l2:
            if l1.val < l2.val:
                res.next = l1
                l1 = l1.next
            else:
                res.next = l2
                l2 = l2.next
            res = res.next
        if l1:
            res.next = l1
        if l2:
            res.next = l2
        return temp.next
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        left, right = self.get_middle_node(head)
        sorted_left = self.sortList(left)
        sorted_right = self.sortList(right)
        return self.merge_lists(sorted_left, sorted_right)

l = ListNode(4)
l.next = ListNode(2)
l.next.next = ListNode(1)
l.next.next.next = ListNode(3)

s = Solution()
sorted_list = s.sortList(l)
print(sorted_list)