# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr.next is not None:
            

l=ListNode(1)
l.next=ListNode(2)
l.next.next=ListNode(3)
l.next.next.next=ListNode(3)
l.next.next.next.next=ListNode(4)
l.next.next.next.next.next=ListNode(4)
l.next.next.next.next.next.next=ListNode(5)

s = Solution()
print(s.deleteDuplicates(l))
