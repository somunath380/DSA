# https://leetcode.com/problems/maximum-product-difference-between-two-pairs/description/

def maxProductDifference(nums: list):
    nums.sort()
    return (nums[-1]*nums[-2]) - (nums[0]*nums[1])

nums = [4,2,5,9,7,4,8]
print(maxProductDifference(nums))
