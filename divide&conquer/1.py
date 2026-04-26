# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def return_mid_node(nums):
            if not nums:
                return
            n = len(nums)
            mid_index = n//2
            mid_node = TreeNode(nums[mid_index])
            left_node = return_mid_node(nums[:mid_index])
            right_node = return_mid_node(nums[mid_index+1:])
            mid_node.left = left_node
            mid_node.right = right_node
            return mid_node
        return return_mid_node(nums)

nums = [-10,-3,0,5,9]
s = Solution()
print(s.sortedArrayToBST(nums))