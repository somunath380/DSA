#https://leetcode.com/problems/determine-if-string-halves-are-alike/description/
def halvesAreAlike(s: str) -> bool:
    n = len(s)
    n1 = (n // 2) - 1
    n1_count, n2_count = 0,0
    vowels = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
    for i in range(n):
        ch = s[i]
        if vowels.get(ch.lower()):
            if i <= n1:
                n1_count += 1
            else:
                n2_count +=1
    return n1_count == n2_count

s = 'textbook'
print(halvesAreAlike(s))