# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/description/

def countGoodSubstrings(s):
    k = 3
    good_substr_count = 0
    substr_k = ""
    for i in range(k-1, len(s)):
        substr_k = s[(i+1)-k:i+1]
        if len(set(substr_k)) == 3:
            good_substr_count += 1
    return good_substr_count

s = "aababcabc"
print(countGoodSubstrings(s))
