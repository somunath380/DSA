#https://leetcode.com/problems/peak-index-in-a-mountain-array/description/

def find_peak_index(arr):
    n = len(arr)-1
    lo, hi = 0, n
    while lo<hi:
        mid = (lo+hi)//2
        if arr[mid] < arr[mid+1]:
            lo = mid+1
        else:
            hi = mid
    return hi

arr = [0,1,0]
print(find_peak_index(arr))
