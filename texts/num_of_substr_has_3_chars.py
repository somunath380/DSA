# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/

def brute_force(s):
    total_count = 0
    char_set = set('abc')
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substr = s[i:j]
            if char_set - set(substr) == set():
                total_count += 1
    return total_count

def two_pointer(s):
    count = 0
    char_set = set('abc')
    i, j = 0, 0
    while j < len(s):
        while char_set - set(s[i:j+1]) == set(): # this will not work as building a new set from substr of len(n) makes o(n) time so total time is o(n)^2
            count += 1 + ((len(s)-1) - j)
            i += 1
        j+=1
    return count

def advance(s: str):
    count = 0
    last = {'a': -1, 'b': -1, 'c': -1}
    for i, ch in enumerate(s):
        last[ch] = i
        if -1 not in last.values():
            count += 1 + min(last.values())
    return count

s = 'abcabc'
print(advance(s))

