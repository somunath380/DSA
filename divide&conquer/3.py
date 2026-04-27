# https://leetcode.com/problems/maximum-subarray/description/
from typing import List

def maxSubArray(nums: List[int]) -> int:
    n=len(nums)
    if n == 1:
        return nums[0]
    prev_sum, max_sum=float('-inf'), float('-inf')
    for i in range(n):
        curr_sum = max(nums[i], prev_sum+nums[i])
        max_sum = max(max_sum, curr_sum)
        prev_sum=curr_sum
    return max_sum

nums = [-2,-1]
print(maxSubArray(nums))