import sys
N = int(sys.stdin.readline())
raw = []

# for i in range(N):
#     num = int(sys.stdin.readline())
#     raw.append(num) # 이렇게 하면 메모리 초과남

def counting_sort(raw):
    counting_arr = [0] * 10001 # max값으로 받으면 10000000까지의 배열 만들어질 수 있고 그건 240MB

    # counting_arr에 raw 내 원소의 빈도수 담기
    for _ in range(N):
        counting_arr[int(sys.stdin.readline())] += 1

    for l in range(len(counting_arr)): # 0 ~ 10000 돌면서
        for _ in range(counting_arr[l]): # 인덱스 1의 값이 4라면 4번 돌면서 각각을 출력
            print(l)

counting_sort(raw)


        


        