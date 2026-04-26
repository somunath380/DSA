# https://leetcode.com/problems/longest-nice-substring/description/

def longestNiceSubstring(s):
    if len(s) < 2:
        return ""
    chars = set(s)
    problematic = None
    for ch in chars:
        if ch.islower() and ch.upper() not in chars:
            problematic = ch
            break
        if ch.isupper() and ch.lower() not in chars:
            problematic = ch
            break
    if problematic is None:
        return s
    parts = s.split(problematic)
    result = ""
    for part in parts:
        candidate = longestNiceSubstring(part)
        if len(candidate) > len(result):
            result = candidate
    return result


s = 'YazaAay'
print(longestNiceSubstring(s))