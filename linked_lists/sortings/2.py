# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        dummy = ListNode(-1)
        prev = dummy
        while curr is not None:
            temp = curr
            while curr.next is not None and curr.val == curr.next.val: # check if curr node is part of duplicate
                curr = curr.next
                continue
            if curr is temp: # if inner loop never runned means the curr is a unique node
                prev.next = curr
                prev = curr
                curr = curr.next
            else: # inner loop runned and curr is duplicate
                curr = curr.next
                prev.next = curr
        return dummy.next
            

l=ListNode(1)
l.next=ListNode(2)
l.next.next=ListNode(3)
l.next.next.next=ListNode(3)
l.next.next.next.next=ListNode(4)
l.next.next.next.next.next=ListNode(4)
l.next.next.next.next.next.next=ListNode(5)

s = Solution()
print(s.deleteDuplicates(l))
