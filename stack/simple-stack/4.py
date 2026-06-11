# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/
def removeDuplicates(s: str) -> str:
    stack=[]
    for ch in s:
        skip=False
        while stack and stack[-1] == ch:
            stack.pop()
            skip=True
        if not skip:
            stack.append(ch)
    return ''.join(stack)

s="azxxzy"
print(removeDuplicates(s))
