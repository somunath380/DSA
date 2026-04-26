# https://leetcode.com/problems/merge-strings-alternately/description/

def mergeAlternatively(word1, word2):
    ans = ''
    n1, n2 = len(word1), len(word2)
    start = 0
    while start < n1 and start < n2:
        ans += word1[start]
        ans += word2[start]
        start += 1
    while start < n1:
        ans += word1[start]
        start += 1
    while start < n2:
        ans += word2[start]
        start += 1
    return ans

word1 = 'abc'
word2 = 'pqr'
print(mergeAlternatively(word1, word2))