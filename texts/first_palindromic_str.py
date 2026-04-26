# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description/

def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left<=right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def firstPalindrome(words):
    for word in words:
        if is_palindrome(word):
            return word
    return ""


def optimize(words):
    for word in words:
        mid = len(word)//2
        if len(word) % 2 == 0: # for when the word has even chars
            if word[:mid] == word[len(word)-1:mid-1:-1]:
                return word
        else: # when it has odd chars
            if word[:mid] == word[len(word)-1:mid:-1]:
                return word
    return ""

words = ["abc","car","ada","racecar","cool"]
print(optimize(words))