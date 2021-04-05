"""

[7, 1, 5, 3, 6, 4] -> 5
"""
nums = [7, 1, 5, 3, 6, 4]

min_p = min(nums)
idx_min = nums.index(min_p)

nums_slice = nums[idx_min:]
max_p = max(nums_slice)

difference = max_p - min_p
print(difference)

# for i in range(1,len(nums)): # 으아 컴마다...
#     # 7 1 1 1 1 1
#     # 7 6 6 6 6 4
#     # ###########
#     # 0 5 5 5 5 3 
