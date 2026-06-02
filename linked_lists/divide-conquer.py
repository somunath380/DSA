# https://leetcode.com/problems/sort-list/description/

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def break_list(head: Optional[ListNode]):
    if not head:
        return
    dummy=ListNode(float('-inf'))
    dummy.next=head
    slow, fast = dummy, head
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
    l2=slow.next
    l1=dummy.next
    slow.next=None
    return l1, l2

def merge_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    if not l1 and l2:
        return
    if l1 is None or l2 is None:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
    dummy = ListNode(float('-inf'))
    tmp=dummy
    while l1 and l2:
        if l1.val < l2.val:
            tmp.next=l1
            l1=l1.next
        else:
            tmp.next=l2
            l2=l2.next
        tmp=tmp.next
    if l1:
        tmp.next=l1
    if l2:
        tmp.next=l2
    return dummy.next

def sortList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return
    if head.next is None:
        return head
    l1, l2 = break_list(head)
    l1_sorted = sortList(l1)
    l2_sorted = sortList(l2)
    return merge_lists(l1_sorted, l2_sorted)

l1 = ListNode(4)
curr=l1
for i in [2,1,3]:
    tmp=ListNode(i)
    curr.next=tmp
    curr=curr.next

res = sortList(l1)
print(res)