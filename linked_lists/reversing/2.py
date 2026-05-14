# https://leetcode.com/problems/reverse-linked-list-ii/description/
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverseBetween(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    if not head.next:
        return head
    dummy = ListNode(-1)
    dummy.next = head
    prev = dummy
    for _ in range(left-1):
        prev = prev.next
    curr = prev.next
    for _ in range(right-left):
        temp = curr.next
        curr.next = temp.next
        temp.next = prev.next
        prev.next = temp
    return dummy.next

