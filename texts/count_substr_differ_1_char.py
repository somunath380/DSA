# https://leetcode.com/problems/count-substrings-that-differ-by-one-character/

def dp_table(s, t):
    n, m = len(s), len(t)
    # suffix[i][j] = longest common suffix starting at position i in s and j in t
    suffix = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if s[i] == t[j]:
                suffix[i][j] = 1 + suffix[i+1][j+1]
            else:
                suffix[i][j] = 0
    
    # prefix[i][j] = longest common prefix ending at position i in s and j in t
    prefix = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s[i-1] == t[j-1]:
                prefix[i][j] = 1 + prefix[i-1][j-1]
            else:
                prefix[i][j] = 0
    
    count = 0
    for i in range(n):
        for j in range(m):
            if s[i] != t[j]:
                # Count all substrings where mismatch is at (i, j)
                # We can extend left by prefix[i][j] characters
                # We can extend right by suffix[i+1][j+1] characters
                count += (prefix[i][j] + 1) * (suffix[i+1][j+1] + 1)
    
    return count

s = "abe"
t = "bbc"

print(dp_table(s, t))
