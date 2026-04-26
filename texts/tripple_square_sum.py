# https://leetcode.com/problems/count-square-sum-triples/description/?envType=daily-question&envId=2025-12-08

from math import gcd, sqrt


def countTriple(n: int) -> int:
    count = 0
    limit = int(sqrt(n))
    for m in range(2, limit):
        for t in (1, m-1):
            if (m-t) % 2 == 0:continue
            if gcd(m,t) != 1: continue
            c0 = m*m + t*t
            if c0 > n: continue
            a0 = m*m - t*t
            b0 = 2*m*t
            max_k = n // c0
            count += 2 * max_k
    return count

n = 5
print(countTriple(n))