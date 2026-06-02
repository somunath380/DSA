# https://leetcode.com/problems/add-two-numbers-ii/description/

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    l1_stack, l2_stack = [], []
    curr1, curr2 = l1, l2
    while curr1:
        l1_stack.append(curr1.val)
        curr1=curr1.next
    while curr2:
        l2_stack.append(curr2.val)
        curr2=curr2.next
    carry=0
    res=[]
    while l1_stack and l2_stack:
        n1 = l1_stack.pop()
        n2 = l2_stack.pop()
        num=n1+n2+carry
        digit=num%10
        res.append(digit)
        carry=num//10
    while l1_stack or l2_stack:
        if l1_stack:
            n1=l1_stack.pop()
            num = n1 + (carry if carry else 0)
        if l2_stack:
            n2=l2_stack.pop()
            num = n2 + (carry if carry else 0)
        digit=num%10
        res.append(digit)
        carry=num//10
    if carry:
        res.append(carry)
    tmp=ListNode(-200)
    dummy=tmp
    while res:
        tmp.next=ListNode(res.pop())
        tmp=tmp.next
    return dummy.next

l1 = ListNode(7)
curr=l1
for i in [2,4,3]:
    tmp=ListNode(i)
    curr.next=tmp
    curr=curr.next

l2 = ListNode(5)
curr=l2
for i in [6,4]:
    tmp=ListNode(i)
    curr.next=tmp
    curr=curr.next

res=addTwoNumbers(l1, l2)
print(res)