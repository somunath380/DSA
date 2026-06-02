# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/description/

from typing import Optional, List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeZeroSumSublists(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy=ListNode(float('-inf'))
    dummy.next=head
    prefix_map={0: dummy}
    curr_sum=0
    curr=head
    while curr:
        curr_sum+=curr.val
        if prefix_map.get(curr_sum):
            prev_node=prefix_map[curr_sum]
            temp=prev_node.next
            temp_sum=curr_sum
            while temp != curr:
                temp_sum+=temp.val
                prefix_map.pop(temp_sum)
                temp=temp.next
            prev_node.next=curr.next
        else:
            prefix_map[curr_sum]=curr
        curr=curr.next
    return dummy.next

l=ListNode(1)
tmp=l
for i in [3,2,-3,-2,5,5,-5,1]:
    tmp.next=ListNode(i)
    tmp=tmp.next

removeZeroSumSublists(l)