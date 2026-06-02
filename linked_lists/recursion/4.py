# https://leetcode.com/problems/swap-nodes-in-pairs/description/

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    def swap(node: Optional[ListNode]) -> Optional[ListNode]:
        if not node:
            return
        if not node.next:
            return node
        first = node
        second = node.next
        next = second.next
        second.next=first
        first.next = swap(next)
        return second
    return swap(head)

l1 = ListNode(1)
curr=l1
for i in [2,3]:
    tmp=ListNode(i)
    curr.next=tmp
    curr=curr.next

li = swapPairs(l1)
print(li)