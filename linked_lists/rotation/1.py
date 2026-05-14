# https://leetcode.com/problems/rotate-list/description/
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_node_counts_and_tail(head: ListNode):
    count, curr = 0, head
    while curr.next:
        count+=1
        curr = curr.next
    return count+1, curr

def rotateRight(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    n, tail = get_node_counts_and_tail(head)
    k=k%n
    if k==0 or not head:
        return head
    counter = n-k-1
    curr, start = head, head
    while counter:
        curr = curr.next
        counter-=1
    new_head = curr.next
    curr.next = None
    tail.next = start
    return new_head

l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)

res = rotateRight(l, 1)
print(res)