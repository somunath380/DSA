# https://leetcode.com/problems/add-two-numbers/description/
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    def get_sum(l1: Optional[ListNode], l2: Optional[ListNode], carry: int)->Optional[ListNode]:
        sum_val=None
        if l1 is None and l2 is None:
            if carry:
                return ListNode(carry)
            return
        elif l1 is None and l2:
            sum_val=l2.val+carry
            l1=None
            l2=l2.next
        elif l2 is None and l1:
            sum_val=l1.val+carry
            l1=l1.next
            l2=None
        else:
            sum_val=l1.val+l2.val+carry
            l1=l1.next
            l2=l2.next
        digit=sum_val%10
        carry=sum_val//10
        node=ListNode(digit)
        node.next=get_sum(l1, l2, carry)
        return node
    return get_sum(l1, l2, 0)


num1=9999999
num2=9999

tmp=ListNode(-1)
l1=tmp
while num1:
    tmp.next=ListNode(num1%10)
    tmp=tmp.next
    num1=num1//10

tmp=ListNode(-1)
l2=tmp
while num2:
    tmp.next=ListNode(num2%10)
    tmp=tmp.next
    num2=num2//10
val=addTwoNumbers(l1.next, l2.next)
print(val)
