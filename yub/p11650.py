import sys
N = int(sys.stdin.readline())

dots = [[0]*2 for i in range(100001)]

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    dots[i][0] = x
    dots[i][1] = y
    
inputs = dots[:N]
# key인자에 함수를 넘겨주면 해당 함수의 반환값을 비교하여 순서대로 정렬
inputs.sort(key=lambda x: (x[0], x[1]))

for i in range(N):
    print(f"{inputs[i][0]} {inputs[i][1]}")

# sorted_xs = sorted(xs)
# # index함수 쓰면 찾는 값의 index 하나만 알 수 있음
# def find_indexs(xs, target):
#     results = []
#     temp_xs = xs
#     while target in temp_xs:
#         index_num = temp_xs.index(target)
#         results.append(ys[index_num])
#         temp_xs[index_num] = 111111 # 범위 밖의 수, del하니까 index가 밀려서 제대로 안 나옴
#     return results

# for j in range(N):
#     temp_list = find_indexs(xs, sorted_xs[j]) # 여기서 시간초과 발생
#     # print(f"temp_list of {sorted_xs[j]} : {temp_list}")
#     if len(temp_list) == 1:
#         value = temp_list[0]
#         print(f"{sorted_xs[j]} {value}")
#     else:
#         sorted_temp_list = sorted(temp_list)
#         for k in range(len(temp_list)):
#             value = sorted_temp_list[k]
#             print(f"{sorted_xs[j]} {value}")