# https://leetcode.com/problems/next-greater-node-in-linked-list/description/

from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def nextLargerNodes(head: Optional[ListNode]) -> List[int]:
    def get_list(head: Optional[ListNode]):
        curr=head
        ans=[]
        while curr:
            ans.append(curr.val)
            curr=curr.next
        return ans
    arr=get_list(head)
    stack=[]
    ans=[0]*len(arr)
    for i in range(len(arr)):
        while stack and arr[i] > arr[stack[-1]]:
            index=stack.pop()
            ans[index]=arr[i]
        stack.append(i)
    return ans

l1 = ListNode(2)
curr=l1
for i in [7,4,3,5]:
    tmp=ListNode(i)
    curr.next=tmp
    curr=curr.next

print(nextLargerNodes(l1))
