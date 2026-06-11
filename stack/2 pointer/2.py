# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/description/

def minSwaps(s: str) -> int:
    min_unmatch=float('inf')
    curr_unmatch=0
    for ch in s:
        if ch == '[':
            curr_unmatch+=1
        else:
            curr_unmatch-=1
        min_unmatch = min(min_unmatch, curr_unmatch)
    min_unmatch=abs(min_unmatch)
    if min_unmatch%2: # odd
        return (min_unmatch//2)+1
    return min_unmatch//2

s = "[]"
print(minSwaps(s))
