def maxConsecutiveAnswers(answerKey: str, k: int) -> int:
    max_len_T = 0
    left, right = 0,0
    max_k_for_T, max_k_for_F = k, k
    while left <= right < len(answerKey):
        if answerKey[right] == 'F':
            max_k_for_T -= 1
        while max_k_for_T <= -1:
            if answerKey[left] == 'F':
                max_k_for_T += 1
            left += 1
        max_len_T = max(max_len_T, (right - left)+1)
        right += 1
    left, right = 0, 0
    max_len_F = 0
    while left <= right < len(answerKey):
        if answerKey[right] == 'T':
            max_k_for_F -= 1
        while max_k_for_F <= -1:
            if answerKey[left] == 'T':
                max_k_for_F += 1
            left += 1
        max_len_F = max(max_len_F, (right - left)+1)
        right += 1
    return max(max_len_F, max_len_T)

answerKey = "TTFTTFTT"
k = 1
print(maxConsecutiveAnswers(answerKey, k))