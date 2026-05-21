# https://leetcode.com/problems/middle-of-the-linked-list/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    slow, fast = head, head
    while fast.next:
        fast=fast.next.next
        slow=slow.next
    return slow

l = ListNode(1)
curr=l
for i in range(2,6):
    tmp=ListNode(i)
    curr.next=tmp
    curr=curr.next
print(middleNode(l))
