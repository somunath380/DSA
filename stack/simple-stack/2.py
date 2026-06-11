# https://leetcode.com/problems/remove-outermost-parentheses/description/

def removeOuterParentheses(s: str) -> str:
    depth=0
    keep=[]
    for ch in s:
        if ch == "(":
            depth+=1
            if depth == 1:
                continue
        else:
            depth -= 1
            if depth == 0:
                continue
        keep.append(ch)
    return ''.join(keep)

s = "()()"
print(removeOuterParentheses(s))