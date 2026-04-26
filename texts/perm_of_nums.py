# https://leetcode.com/problems/permutations/description/

def give_perms(nums: list):
    ans = []
    nums.sort()
    def recur(index, nums):
        if index == len(nums):
            ans.append(nums)
            return
        for i in range(index, len(nums)):
            if nums[index] == nums[i]:
                continue
            nums[index], nums[i] = nums[i], nums[index]
            recur(index+1, nums[:])
            nums[index], nums[i] = nums[i], nums[index]
    recur(0, nums)
    return ans

nums = [1,1,2]
print(give_perms(nums))