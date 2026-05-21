# https://leetcode.com/problems/reorder-list/description/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next is None:
            return head
        head, l2 = self.splitList(head)
        l2 = self.reverseList(l2)
        self.mergeNodes(head, l2)
        return head

    def reverseList(self, head: Optional[ListNode]) -> ListNode:
        tmp_head, curr=head, head
        dummy=ListNode(-1)
        dummy.next=head
        prev=dummy
        while curr.next:
            tmp=curr.next
            curr.next=prev
            prev=curr
            curr=tmp
        curr.next=prev
        tmp_head.next=None
        return curr

    def mergeNodes(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        c1, c2 = l1, l2
        while c1.next and c2.next:
            c1_next, c2_next = c1.next, c2.next
            c1.next=c2
            c2.next=c1_next
            c1=c1_next
            c2=c2_next
        if c2:
            c1_next = c1.next if c1.next else None
            c1.next=c2
            c2.next=c1_next
        elif c1:
            c1.next=c2
        return l1

    def splitList(self, head: Optional[ListNode]):
        """Using slow-fast pointer to find the middle and split the list"""
        slow, fast = head, head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        l2=slow.next
        slow.next=None
        return head, l2

l = ListNode(1)
curr=l
for i in range(2,6):
    tmp=ListNode(i)
    curr.next=tmp
    curr=curr.next

s = Solution()
s.reorderList(l)
print(l)
