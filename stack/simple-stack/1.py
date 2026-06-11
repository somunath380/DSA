# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/

def maxDepth(s: str) -> int:
    seen=[] # stack
    max_depth=0
    for ch in s:
        if ch == "(":
            seen.append("(")
            max_depth = max(max_depth, len(seen))
        elif ch == ")":
            seen.pop()
    return max_depth

s="()(())((()()))"
print(maxDepth(s))