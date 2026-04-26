# https://leetcode.com/problems/kth-distinct-string-in-an-array/
from collections import Counter
def kthDistinct(arr, k: int) -> str:
    distinct_arr = []
    c = Counter(arr)
    for ele in arr:
        if c.get(ele) == 1:
            distinct_arr.append(ele)
    if k-1 > len(distinct_arr) - 1:
        return ""
    return distinct_arr[k-1]

arr = ["d","b","c","b","c","a"]
k = 2
print(kthDistinct(arr, k))