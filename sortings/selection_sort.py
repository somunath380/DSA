
def selection_sort(arr: list) -> list:
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr

arr = [4,2,6,5,1,3]
print(selection_sort(arr))

# [4, 2, 6, 5, 1, 3]
# [0, 1, 2, 3, 4, 5] <- index

# min_index = 2 (index), value = arr[2] = 6

# compare arr[min_index] with every other values

# if any element value is less than arr[min_index] i.e 4 then store the latest index in the min_index

# 2 < 4 min_index = 1

# 6 > 2

# 5 > 2

# 1 < 2 min_index = 4

# 3 > 1 

# we got min_index = 4 i.e arr[min_index] = 1

# so we will swap 4 i.e arr[0] with arr[min_index] i.e 4

# arr = [1, 2, 6, 5, 4, 3]

# now we will strat from min_index = 1 i.e arr[1] = 2 and do the comparison again and find out the smallest number's index'