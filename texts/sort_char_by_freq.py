"""Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

 

Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer."""

from collections import Counter
def frequencySort(s: str) -> str:
    counter = Counter(s)
    ans = ""
    bucket = [[] for _ in range(len(s)+1)]
    for ch, freq in counter.items():
        bucket[freq].append(ch)
    for i in range(len(bucket)-1, 0, -1):
        if bucket[i]:
            for each_ch in bucket[i]:
                ans += each_ch * i
    return ans

s = "eeeee"
print(frequencySort(s))
