nums = [1,2,3,4,5,6,7]

# assumes array sorted

def binary_search(nums, target):
    nums.sort() # optional
    left = 0
    right = len(nums)-1
    while left < right:
        mid = left+right // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid-1
        else:
            left = mid+1
    return "Not found"