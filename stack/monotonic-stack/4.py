# https://leetcode.com/problems/maximum-binary-tree/description/
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def constructMaximumBinaryTree(nums: List[int]) -> Optional[TreeNode]:
    stack: List[TreeNode]=[]
    for i in range(len(nums)):
        current_node=TreeNode(nums[i])
        while stack and stack[-1].val<current_node.val:
            last = stack.pop()
            current_node.left=last
        if stack:
            stack[-1].right=current_node
        stack.append(current_node)
    return stack[0]

nums=[3,2,1,6,0,5]
print(constructMaximumBinaryTree(nums))
