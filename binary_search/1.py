def first_match_binary_search(nums, target):
    lo, hi = 0, len(nums)-1
    idx = -1
    while lo <= hi:
        mid = (lo+hi)//2
        if target <= nums[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
        if nums[mid] == target:
            idx = mid
    return idx

def last_match_binary_search(nums, target):
    lo, hi = 0, len(nums)-1
    idx = -1
    while lo <= hi:
        mid = (lo+hi)//2
        if target >= nums[mid]:
            lo = mid + 1
        else:
            hi = mid - 1
        if nums[mid] == target:
            idx = mid
    return idx

def get_indexes(nums: list, target):
    nums.sort()
    first_index = first_match_binary_search(nums, target)
    if first_index == -1:
        return []
    last_index = last_match_binary_search(nums, target)
    return list(range(first_index, last_index+1)) if last_index != -1 else [first_index]

# optimal solution

def return_indices(nums: list, target: int):
    count_of_less_numbers = 0 # total numbers that are less than the target num = the starting index of the target in nums
    count_of_equals_of_target = 0 # total nums that are equal to target = how many target nums are present in nums
    for num in nums:
        if num < target:
            count_of_less_numbers+=1
        if num == target:
            count_of_equals_of_target+=1
    # so we get the first index of target (in a sorted arr nums), now if we add how many equal target num are there with the starting nums - 1 then we will get the index of the end target nums
    return list(range(count_of_less_numbers, count_of_less_numbers+count_of_equals_of_target))

nums = [1,2,5,2,3]
target = 4
print(return_indices(nums, target))