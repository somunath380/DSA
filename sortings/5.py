# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

def maxProduct(nums: list) -> int:
        max1 = -float('inf')
        max2 = -float('inf')

        for num in nums:
            if num > max1:
                max2 = max1
                max1 = num
            else:
                max2 = max(max2, num)
        
        return (max1 - 1) * (max2 - 1)

nums = [3,4,5,2]
print(maxProduct(nums))