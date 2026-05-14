# https://leetcode.com/problems/split-linked-list-in-parts/description/

from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def get_length(self, head: ListNode):
        n = 0
        curr = head
        while curr:
            n+=1
            curr = curr.next
        return n
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        if not head: return []*k
        n = self.get_length(head)
        base_size = n//k
        remainder = n%k
        result = []
        curr = head
        for i in range(k):
            size = base_size+(1 if remainder>0 else 0)
            remainder -= 1 if remainder > 0 else 0
            count = size-1
            if not curr:
                result.append(None)
                continue
            result.append(curr)
            for _ in range(count):
                curr=curr.next
            next_head = curr.next
            curr.next=None
            curr=next_head
        return result

l = ListNode(1)
temp=l
for i in range(2,11):
    new_node = ListNode(i)
    temp.next = new_node
    temp=temp.next

s=Solution()
print(s.splitListToParts(l,3))
