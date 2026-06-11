# https://leetcode.com/problems/next-greater-element-i/description/
from typing import List

def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    stack=[]
    ans={}
    for i in range(len(nums2)):
        while stack and nums2[i]>nums2[stack[-1]]:
            index=stack.pop()
            ans[nums2[index]]=nums2[i]
        stack.append(i)
    res=[]
    for j in nums1:
        res.append(ans[j] if ans.get(j) else -1)
    return res
nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(nextGreaterElement(nums1, nums2))
