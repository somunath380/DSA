# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr.next is not None:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

l=ListNode(1)
l.next=ListNode(1)
l.next.next=ListNode(1)
l.next.next.next=ListNode(2)
l.next.next.next.next=ListNode(3)
l.next.next.next.next.next=ListNode(3)

s=Solution()
s.deleteDuplicates(l)
print(s)
