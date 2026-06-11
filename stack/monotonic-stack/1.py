# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

from typing import List

def finalPrices(prices: List[int]) -> List[int]:
    stack=[]
    discounts=[0]*len(prices)
    for i in range(len(prices)):
        while stack and prices[i]<=prices[stack[-1]]:
            idx=stack.pop()
            discounts[idx]=prices[i]
        stack.append(i)
    return [x-y for x, y in zip(prices, discounts)]
prices=[10,1,1,6]
print(finalPrices(prices))
