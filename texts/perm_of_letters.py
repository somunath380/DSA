
def perm_of_letters(s):
    ans = []
    def recursion(index, s, ans):
        if index == len(s):
            ans.append(''.join(s))
            return
        for i in range(index, len(s)):
            s[index], s[i] = s[i], s[index]
            recursion(index+1, s, ans)
            s[index], s[i] = s[i], s[index]
    recursion(0, list(s), ans)
    return ans

s = "abc"
print(perm_of_letters(s))