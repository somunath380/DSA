def bubble_sort(arr: list) -> list:
    n = len(arr)
    for external_loop_no in range(n-1, 0, -1):
        for internal_loop_no in range(external_loop_no):
            if arr[internal_loop_no] > arr[internal_loop_no+1]:
                arr[internal_loop_no], arr[internal_loop_no+1] = \
                    arr[internal_loop_no+1], arr[internal_loop_no]
    return arr

arr = [4,2,6,5,1,3]
print(bubble_sort(arr))

# [4,2,6,5,1,3] -> [1,2,3,4,5,6]

# [2,4,6,5,1,3]
# [2,4,6,5,1,3]
# [2,4,5,6,1,3]
# [2,4,5,1,6,3]
# [2,4,5,1,3,     6]

# [2,4,5,1,3,  6]
# [2,4,5,1,3,  6]
# [2,4,1,5,3,  6]
# [2,4,1,3,  5,6]

# [2,4,1,3,  5,6]
# [2,1,4,3,  5,6]
# [2,1,3,  4,5,6]

# [1,2,3,  4,5,6]
# [1,2,  3,4,5,6]

# [1,  2,3,4,5,6]

# external_loop_no = n - 1

# internal_loop_no = external_loop_no - 1