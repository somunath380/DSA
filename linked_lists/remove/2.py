# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(-1)
        dummy.next=head
        fast=dummy
        slow=dummy
        for _ in range(n):
            fast=fast.next
        while fast.next:
            slow=slow.next
            fast=fast.next
        target=slow.next
        next_node=target.next
        slow.next=next_node
        target.next=None
        return dummy.next

s=Solution()

l=ListNode(1)
l.next=ListNode(2)
# l.next.next=ListNode(3)
# l.next.next.next=ListNode(4)
# l.next.next.next.next=ListNode(5)
# l.next.next.next.next.next=ListNode(5)
# l.next.next.next.next.next.next=ListNode(6)

print(s.removeNthFromEnd(l, 1))
