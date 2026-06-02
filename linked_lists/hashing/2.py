# https://leetcode.com/problems/linked-list-components/description/

from typing import Optional, List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def numComponents(head: Optional[ListNode], nums: List[int]) -> int:
    comps = 0
    curr=head
    while curr:
        if curr.val in nums and (curr.next is None or curr.next.val not in nums):
            comps+=1
        curr=curr.next
    return comps

l1 = ListNode(0)
curr=l1
for i in [1,2,3]:
    tmp=ListNode(i)
    curr.next=tmp
    curr=curr.next

print(numComponents(l1, [0,1,3]))