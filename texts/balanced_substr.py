#https://leetcode.com/problems/split-a-string-in-balanced-strings/description/

def balancedStringSplit(s: str) -> int:
    count = 0
    r_count = 0
    l_count = 0
    for ch in s:
        if ch == "R":
            r_count += 1
        else:
            l_count += 1
        if l_count == r_count:
            count += 1
            l_count, r_count = 0,0
    return count
s = "RLRRRLLRLL"
print(balancedStringSplit(s))