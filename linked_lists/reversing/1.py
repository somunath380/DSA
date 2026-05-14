# https://leetcode.com/problems/reverse-linked-list/description/
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return
    prev_node, curr, next_node = None, head, head.next
    while curr.next:
        curr.next = prev_node
        prev_node = curr
        temp = next_node.next
        curr = next_node
        next_node=temp
    curr.next=prev_node
    return curr

l=ListNode(1)

res = reverseList(l)
print(res)