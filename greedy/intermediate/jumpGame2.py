"""
Jump game 2

"""

def jump(nums):
    jumps = 0
    cur_end = cur_farthest = 0
    for i in range(len(nums) - 1):
        cur_farthest = max(cur_farthest, i + nums[i])
        if i == cur_end:
            jumps += 1
            cur_end = cur_farthest
    return jumps
