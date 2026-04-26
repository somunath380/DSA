"""
Code
Testcase
Testcase
Test Result
1370. Increasing Decreasing String
Easy
Topics
premium lock icon
Companies
Hint
You are given a string s. Reorder the string using the following algorithm:

Remove the smallest character from s and append it to the result.
Remove the smallest character from s that is greater than the last appended character, and append it to the result.
Repeat step 2 until no more characters can be removed.
Remove the largest character from s and append it to the result.
Remove the largest character from s that is smaller than the last appended character, and append it to the result.
Repeat step 5 until no more characters can be removed.
Repeat steps 1 through 6 until all characters from s have been removed.
If the smallest or largest character appears more than once, you may choose any occurrence to append to the result.

Return the resulting string after reordering s using this algorithm.

 

Example 1:

Input: s = "aaaabbbbcccc"
Output: "abccbaabccba"
Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
After steps 4, 5 and 6 of the first iteration, result = "abccba"
First iteration is done. Now s = "aabbcc" and we go back to step 1
After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"""

# brute force
def sortString(s):
    frq_dict = {}
    for ch in s:
        frq_dict[ch] = frq_dict.get(ch, 0) + 1
    ans = ""
    sorted_chars = sorted(set(frq_dict.keys()))
    start = 0
    asc = True
    desc = False
    while sum(frq_dict.values())!= 0: # adding condition later
        if start < 0:
            asc = True
            desc = False
            start += 1
            continue
        if start > len(sorted_chars) - 1:
            asc = False
            desc = True
            start -= 1
            continue
        char = sorted_chars[start]
        if frq_dict.get(char, 0): # get freq of char
            ans += char
            frq_dict[char] -= 1
        if asc:
            start += 1
        elif desc:
            start -= 1
    return ans

from collections import Counter
def optimized(s):
    count = Counter(s)
    sorted_chars = sorted(count.keys())
    result = []
    total = len(s)
    
    while total > 0:
        # Forward pass: smallest to largest
        for char in sorted_chars:
            if count[char] > 0:
                result.append(char)
                count[char] -= 1
                total -= 1
        
        # Backward pass: largest to smallest
        for char in reversed(sorted_chars):
            if count[char] > 0:
                result.append(char)
                count[char] -= 1
                total -= 1
    
    return ''.join(result)

s = "aaaabbbbcccc"
print(optimized(s))
