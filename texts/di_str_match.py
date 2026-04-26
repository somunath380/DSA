#https://leetcode.com/problems/di-string-match/description/

def diStringMatch(s: str):
    n = len(s)
    start = 0
    end = n
    str_start = 0
    ans = [None] * (end+1)
    while str_start<n and start < end:
        str_ch = s[str_start]
        if str_ch == 'I':
            ans[str_start] = start
            start += 1
        else:
            ans[str_start] = end
            end -= 1
        str_start += 1
    ans[str_start] = end
    return ans

print(diStringMatch("III"))