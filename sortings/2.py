# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

def smallerNumbersThanCurrent(nums: list) -> list:
    nums_sorted = sorted(nums)
    num_index_map = {}
    for i in range(len(nums_sorted)):
        if nums_sorted[i] in num_index_map:
            continue
        num_index_map[nums_sorted[i]] = i
    ans = []
    for num in nums:
        ans.append(num_index_map[num])
    return ans

nums = [8, 1, 2, 2, 3]

print(smallerNumbersThanCurrent(nums))

