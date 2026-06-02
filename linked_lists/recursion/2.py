# https://leetcode.com/problems/merge-two-sorted-lists/description/

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    def merge(l1: Optional[ListNode], prev1: Optional[ListNode], l2: Optional[ListNode], prev2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            l1.next = merge(l1.next, prev1.next, l2, prev2)
            return l1
        else:
            l2.next = merge(l1, prev1, l2.next, prev2.next)
            return l2
    dummy1, dummy2=ListNode(-200), ListNode(-200)
    dummy1.next, dummy2.next=list1, list2
    head = merge(list1, dummy1, list2, dummy2)
    return head

l1 = ListNode(2)
curr=l1
for i in [3,4]:
    tmp=ListNode(i)
    curr.next=tmp
    curr=curr.next

l2 = ListNode(1)
curr=l2
for i in [2,3]:
    tmp=ListNode(i)
    curr.next=tmp
    curr=curr.next

ans = mergeTwoLists(l1, l2)
print(ans)