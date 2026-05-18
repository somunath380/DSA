# https://leetcode.com/problems/remove-linked-list-elements/description/
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    prev = ListNode(-1)
    temp=prev
    curr = head
    while curr:
        if curr.val != val:
            prev.next=curr
        else:
            curr=curr.next
            continue
        prev=curr
        curr=curr.next
    prev.next=None
    curr_head = temp.next
    temp.next=None
    return curr_head

l=ListNode(7)
l.next=ListNode(7)
l.next.next=ListNode(7)
# l.next.next.next=ListNode(3)
# l.next.next.next.next=ListNode(4)
# l.next.next.next.next.next=ListNode(5)
# l.next.next.next.next.next.next=ListNode(6)

removeElements(l, 7)
