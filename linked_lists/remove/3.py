# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return
    dummy=ListNode(-200)
    dummy.next=head
    curr, prev=head, dummy
    while curr:
        loop_ran=False # this decides if the curr node after the inner loop is part of a duplicate ornot
        while curr.next and curr.val == curr.next.val:
            loop_ran=True
            curr=curr.next
        if loop_ran:
            curr=curr.next
            prev.next=curr
        else:
            prev.next=curr
            curr=curr.next
            prev=curr
    return dummy.next

l=ListNode(1)
l.next=ListNode(1)
# l.next.next=ListNode(3)
# l.next.next.next=ListNode(3)
# l.next.next.next.next=ListNode(4)
# l.next.next.next.next.next=ListNode(4)
# l.next.next.next.next.next.next=ListNode(5)

print(deleteDuplicates(l))