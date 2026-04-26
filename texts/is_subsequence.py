# https://leetcode.com/problems/is-subsequence/description/

def isSubsequence(s: str, t: str) -> bool:
    if not s:
        return True
    chars = [s[i] for i in range(len(s)-1, -1, -1)]
    for ch in t:
        if chars and ch == chars[-1]:
            chars.pop()
            continue
    if not chars:
        return True
    return False

s = "b"
t = "abc"
print(isSubsequence(s,t))