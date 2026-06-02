# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    def recurse(node: Optional[ListNode]) -> Optional[ListNode]:
        if not node:
            return
        if not node.next:
            return node
        if node.val == node.next.val:
            return recurse(node.next)
        else:
            node.next = recurse(node.next)
        return node
    return recurse(head)

l1 = ListNode(1)
curr=l1
for i in [1,2]:
    tmp=ListNode(i)
    curr.next=tmp
    curr=curr.next

res=deleteDuplicates(l1)
print(res)
