# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/description/


def minimumSum(num: int) -> int:
    digits = []
    while num:
        digits.append(num%10)
        num = num//10
    digits.sort()
    new1, new2 = digits[0]*10+digits[2], digits[1]*10+digits[3]
    return new1+new2

num = 2923
print(minimumSum(num))
