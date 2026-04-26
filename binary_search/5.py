# https://leetcode.com/problems/intersection-of-two-arrays/description/

def find_intersected_elements(arr1: list, arr2: list) -> list:
    n1, n2 = len(arr1), len(arr2)
    arr = None
    res = set()
    if n1 <= n2:
        s = set(arr1)
        arr = arr2
    else:
        s = set(arr2)
        arr = arr1
    for n in arr:
        if n in s:
            res.add(n)
            s.remove(n)
    return list(res)

arr1 = [4,9,5]
arr2 = [9,4,9,8,4]

print(find_intersected_elements(arr1, arr2))
