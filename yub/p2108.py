import sys
from collections import Counter
N = int(sys.stdin.readline())
nums = []
for _ in range(N):
    num = int(sys.stdin.readline())
    nums.append(num)

avg_s = round(sum(nums) / N)

sorted_nums = sorted(nums)
avg_j = sorted_nums[N // 2]

mod = Counter(nums)
mod_nums = mod.most_common()
mod_nums.sort(key=lambda x:(-x[1], x[0])) # -달면 내림차순
# print(mod_nums)
if N == 1:
    avg_c = mod_nums[0][0]
else:
    if mod_nums[0][1] == mod_nums[1][1]:
        avg_c = mod_nums[1][0]
    else:
        avg_c = mod_nums[0][0]

avg_r = max(nums) - min(nums)

print(avg_s)
print(avg_j)
print(avg_c)
print(avg_r)