# https://leetcode.com/problems/odd-even-linked-list/description/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd, even = head, head.next
        even_head = head.next
        while even and even.next:
            odd.next=even.next
            odd=odd.next
            even.next=odd.next
            even=even.next
        odd.next=even_head
        return head
        # curr = head.next.next
        # is_odd=True
        # while curr:
        #     if is_odd:
        #         odd.next=curr
        #         odd=odd.next
        #         is_odd=False
        #     else:
        #         even.next=curr
        #         even=even.next
        #         is_odd=True
        #     curr=curr.next
        # odd.next=head.next
        # return head

l = ListNode(1)
curr=l
for i in range(2,6):
    tmp=ListNode(i)
    curr.next=tmp
    curr=curr.next

s = Solution()
print(s.oddEvenList(l))
