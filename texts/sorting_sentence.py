def sortSentence(s: str) -> str:
    idx_word_map = {}
    for word in s.split(' '):
        idx_word_map[int(word[-1])] = word[:-1:]
    ans = ''
    for idx in sorted(idx_word_map.keys()):
        ans += idx_word_map[idx] + ' '
    return ans.removesuffix(' ')

s = "is2 sentence4 This1 a3"
print(sortSentence(s))