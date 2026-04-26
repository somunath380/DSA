
def reversePrefix(word: str, ch: str) -> str:
    word = list(word)
    for i in range(len(word)):
        if word[i] == ch:
            start = 0
            end = i
            while start <= end:
                word[start], word[end] = word[end], word[start]
                start += 1
                end -= 1
            break
    return ''.join(word)

word = "abcdefgd"
print(reversePrefix(word, 'd'))