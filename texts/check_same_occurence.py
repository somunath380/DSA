#https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/
from collections import Counter
def areOccurrencesEqual(s: str) -> bool:
    # c = {}
    # for ch in s:
    #     c[ch] = c.get(ch, 0) + 1
    # for i in range(1, len(c.keys())):
    #     if 
    # ch_iter = list(c.keys())
    # freq_iter = list(c.values())
    # first_ch, first_ch_freq = ch_iter[0], freq_iter[0]
    # for i in range(1, len(ch_iter)):
    #     if first_ch_freq != ch_iter[i]:
    #         return False
    # return True
    c = Counter(s)
    freq = list(c.values())
    for i in range(1, len(c.values())):
        if freq[i] != freq[i-1]:
            return False
    return True

s = "juczjzjlsfkmpv"
print(areOccurrencesEqual(s))