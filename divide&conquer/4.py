# https://leetcode.com/problems/reverse-bits/
def reverseBits(n: int) -> int:
    res = 0
    for i in range(31):
        last_bit = n & 1
        res = res | last_bit
        res = res << 1
        n = n >> 1
    return res

def divide_and_conquer(n: int):
    def recurse(n, bit_len):
        if bit_len == 1:
            return n
        half=bit_len//2
        mask=(1<<half)-1
        right_half=n&mask
        left_half=n>>half
        left=recurse(left_half, half)
        right=recurse(right_half, half)
        return right<<half|left
    return recurse(n, 4)

n=5
print(divide_and_conquer(n))