# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/description/
from heapq import heappush, heappop

def find_last_one(arr):
    index = -1
    low, hi = 0, len(arr)-1
    while low <= hi:
        mid = (low+hi)//2
        if arr[mid] == 1:
            index = mid
            low = mid + 1
        else:
            hi = mid - 1
    return index

def kWeakestRows(mat, k):
    nums = []
    for row in mat:
        index = find_last_one(row)
        nums.append(index+1)
    heap = []
    for i in range(len(nums)):
        # num = nums[i]
        if len(heap) > k-1:
            heappop(heap)
        heappush(heap, i)
    return list(heap)


mat = [ [1,1,0,0,0],
        [1,1,1,1,0],
        [1,0,0,0,0],
        [1,1,0,0,0],
        [1,1,1,1,1]
    ]

k = 3
print(kWeakestRows(mat, k))
