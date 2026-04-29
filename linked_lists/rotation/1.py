# https://leetcode.com/problems/rotate-list/description/
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_node_counts(head: ListNode):
    count, curr = 0, head
    while curr:
        count+=1
        curr = curr.next
    return count

def rotateRight(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    n = get_node_counts(head)
    if k==0 or k%n == 0:
        return head
    if k>n:
        k = n-k
    curr, last = head, head
    while last.next:
        last = last.next
    prev = ListNode()
    while k and curr.next: # will get prev which will be last node and curr which will be head
        prev = curr
        curr = curr.next
        k-=1
    prev.next = None
    new_head = curr
    last.next = head
    return new_head

l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)

res = rotateRight(l, 1)
print(res)