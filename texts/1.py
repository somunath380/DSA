# https://leetcode.com/problems/count-the-number-of-consistent-strings/description/

def countConsistentStrings(allowed, words):
    mask = 0
    count = 0
    for c in allowed:
        mask |= 1 << (ord(c) - ord('a'))
    for word in words:
        valid = True
        for char in word:
            if (mask & (1 << (ord(char) - ord('a')))) == 0:
                valid = False
                break
        if valid:
            count += 1
    return count

allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
print(countConsistentStrings(allowed, words))
