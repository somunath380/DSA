# https://leetcode.com/problems/intersection-of-two-linked-lists/description/

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    def get_len(head: Optional[ListNode]):
        n=0
        tmp=head
        while tmp:
            n+=1
            tmp=tmp.next
        return n
    n1=get_len(headA)
    n2=get_len(headB)
    if n1>n2:
        n=n1-n2
        tmp=headA
        for _ in range(n):
            tmp=tmp.next
        p1=tmp
        p2=headB
    else:
        n=n2-n1
        tmp=headB
        for _ in range(n):
            tmp=tmp.next
        p1=headA
        p2=tmp
    while p1 and p2:
        if p1 is p2:
            return p1
        p1=p1.next
        p2=p2.next
    return

l=ListNode(8)
l.next=ListNode(4)
l.next.next=ListNode(5)

l1=ListNode(4)
l1.next=ListNode(1)
l1.next.next=l

l2=ListNode(5)
l2.next=ListNode(6)
l2.next.next=ListNode(1)
l2.next.next.next=l

print(getIntersectionNode(l1, l2).val)