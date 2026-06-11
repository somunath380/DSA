# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        p2 = self.findMid(head)
        second_list=p2.next
        p2.next=None
        second_list=self.reverse(second_list)
        max_sum=0
        p1, p2 = head, second_list
        while p1 and p2:
            curr_sum = p1.val + p2.val
            max_sum = max(max_sum, curr_sum)
            p1=p1.next
            p2=p2.next
        return max_sum

    def findMid(self, head: Optional[ListNode]):
        dummy=ListNode(float('-inf'))
        dummy.next=head
        slow, fast=dummy, dummy
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        return slow

    def reverse(self, head: Optional[ListNode]):
        curr=head
        prev=None
        while curr.next:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        curr.next=prev
        return curr

