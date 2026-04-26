# https://leetcode.com/problems/sorting-the-sentence/description/

def sortSentence(s: str):
    words = s.split(' ')
    ans = ['']*len(words)
    for word in words:
        n = len(word)
        idx = int(word[-1])-1
        ans[idx] = word[:n-1]
    return ' '.join(ans)

s = "is2 sentence4 This1 a3"
print(sortSentence(s))

