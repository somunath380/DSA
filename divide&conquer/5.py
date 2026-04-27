# https://leetcode.com/problems/maximum-binary-tree/description/
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def find_index_of_max_val(self, nums):
        max_val, max_index=float('-inf'), 0
        for i in range(len(nums)):
            if nums[i]>max_val:
                max_index=i
                max_val=nums[i]
        return max_index
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def get_root_node(nums):
            n = len(nums)
            if n == 0:
                return
            max_index = self.find_index_of_max_val(nums)
            root_node = TreeNode(nums[max_index])
            left_arr = nums[:max_index]
            right_arr = nums[max_index+1:]
            left_root = get_root_node(left_arr)
            right_root = get_root_node(right_arr)
            root_node.left = left_root
            root_node.right = right_root
            return root_node
        return get_root_node(nums)

nums = [3,2,1,6,0,5]
s=Solution()
print(s.constructMaximumBinaryTree(nums))
