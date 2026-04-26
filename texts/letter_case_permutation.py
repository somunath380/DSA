# https://leetcode.com/problems/letter-case-permutation/description/

def perm(s: str):
    result = []
    def backtrack(index, path):
        if index == len(s):
            result.append(path)
            return
        char = s[index]
        if char.isdigit():
            backtrack(index+1, path+char)
        else:
            backtrack(index+1, path+char.lower())
            backtrack(index+1, path+char.upper())
    backtrack(0, "")
    return result

s = 'a1b2'
print(perm(s))
