# https://leetcode.com/problems/trapping-rain-water/description/
from typing import List

def trap(arr: List[int]) -> int:
    n=len(arr)
    left, right=0, n-1
    max_left=float('-inf')
    max_right=float('-inf')
    water=0
    while left<=right:
        max_left=max(max_left, arr[left])
        max_right=max(max_right, arr[right])
        if max_left<=max_right:
            water+=max_left - arr[left]
            left+=1
        else:
            water+=max_right-arr[right]
            right-=1
    return water
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))
