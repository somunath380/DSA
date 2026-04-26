"""Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.

 

Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and b map to the same letter.
Example 2:

Input: words = ["a","b","c"], pattern = "a"
Output: ["a","b","c"]"""
from typing import List
def encode(word):
    char_to_number = {}
    result = []
    next_num = 0
    for ch in word:
        if char_to_number.get(ch, -1) == -1:
            char_to_number[ch] = next_num
            result.append(next_num)
            next_num+=1
        else:
            result.append(char_to_number[ch])
    return result

def findAndReplacePattern(words: List[str], pattern: str) -> List[str]:
    canonically_converted_pattern = encode(pattern)
    ans = []
    for word in words:
        if canonically_converted_pattern == encode(word):
            ans.append(word)
    return ans

words = ["ccc"]
pattern = "abb"

print(findAndReplacePattern(words, pattern))