# https://leetcode.com/problems/majority-element/description/

from typing import List

def majorityElement(nums: List[int]) -> int:
    var, count = nums[0], 1
    for i in range(1, len(nums)):
        ele = nums[i]
        if ele == var:
            count+=1
        else:
            count -= 1
            if count == 0:
                var = ele
                count = 1
    return var


nums = [3,2,3]
print(majorityElement(nums))