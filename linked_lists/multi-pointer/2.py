# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteMiddle(head: Optional[ListNode]) -> Optional[ListNode]:
    if head.next is None:
        return
    dummy=ListNode(-1)
    dummy.next=head
    slow, fast=dummy, head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    slow.next=slow.next.next
    dummy.next=None
    return head

l = ListNode(1)
# curr=l
# for i in [3,4,7,1,2,6]:
#     tmp=ListNode(i)
#     curr.next=tmp
#     curr=curr.next

print(deleteMiddle(l))
