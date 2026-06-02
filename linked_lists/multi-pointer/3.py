# https://leetcode.com/problems/partition-list/description/
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head: return
        less = ListNode(-200)
        less_head=less
        greater = ListNode(-200)
        greater_head=greater
        curr = head
        while curr:
            if curr.val<x:
                less.next=curr
                less=less.next
            else:
                greater.next=curr
                greater=greater.next
            curr=curr.next
        greater.next=None
        less.next=greater_head.next
        return less_head.next

l = ListNode(1)
# curr=l
# for i in [1]:
#     tmp=ListNode(i)
#     curr.next=tmp
#     curr=curr.next

s = Solution()
s.partition(l, 0)
