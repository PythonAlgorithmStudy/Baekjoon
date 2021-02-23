import sys

N = int(sys.stdin.readline())
raw = []

for j in range(N):
    num = int(sys.stdin.readline())
    raw.append(num)
arr = sorted(raw) 
# 프로그래밍 언어 차원에서 기본적으로 지원되는 내장 정렬함수는 대부분 퀵정렬을 기본으로 함
for i in arr:
    print(i)
# pypy3로 제출하였음

# def merge_divide(raw):
#     if len(raw) <= 1:
#         return raw

#     mid = len(raw) // 2
#     left = raw[:mid]
#     right = raw[mid:]

#     left1 = merge_divide(left)
#     right1 = merge_divide(right)
#     return merge(left1, right1)

# def merge(left, right):
#     i = 0
#     j = 0
#     sorted_list = []

#     while (i < len(left)) & (j<len(right)):
#         if left[i] < right[j]:
#             sorted_list.append(left[i])
#             i += 1
#         else:
#             sorted_list.append(right[j])
#             j += 1
#     # i, j 중 하나는 끝을 본 상황
#     while (i<len(left)):
#         sorted_list.append(left[i])
#         i += 1
#     while (j<len(right)):
#         sorted_list.append(right[j])
#         j += 1

#     return sorted_list

# print(merge_divide(raw))
