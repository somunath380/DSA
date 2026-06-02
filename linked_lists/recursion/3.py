# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/description/

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getDecimalValue(head: Optional[ListNode]) -> int:
    def dfs(node, curr):
        if not node:
            return curr
        curr = curr * 2 + node.val
        return dfs(node.next, curr)
    return dfs(head, 0)

l1 = ListNode(1)
curr=l1
for i in [0,1]:
    tmp=ListNode(i)
    curr.next=tmp
    curr=curr.next

print(getDecimalValue(l1))