# https://leetcode.com/problems/maximum-score-of-a-good-subarray/description/
from typing import List

def maximumScore(nums: List[int], k: int) -> int:
    left, right, n = k, k, len(nums)
    max_score=nums[k]
    min_val=nums[k]
    while left>=1 or right<=n-2:
        if left==0 and right<n-1:
            right+=1
            min_val=min(nums[right], min_val)
        elif right==n-1 and left>=1:
            left-=1
            min_val=min(nums[left], min_val)
        elif nums[right+1]>=nums[left-1]:
            right+=1
            min_val=min(nums[right], min_val)
        else:
            left-=1
            min_val=min(nums[left], min_val)
        dist=(right-left+1)
        val=min_val*dist
        max_score=max(max_score, val)
    return max_score


nums = [5,5,4,5,4,1,1,1]
k = 0
print(maximumScore(nums, k))