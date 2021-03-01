import sys
N = int(sys.stdin.readline())

words = [[0]*2 for i in range(100001)]
for i in range(N):
    word = str(input()) # input쓰면 엔터 안 받아옴
    words[i][0] = word
    words[i][1] = len(word)

inputs = words[:N]
# 중복 제거
# 튜플은 hashable한 자료형이어서 2차원 튜플에 set함수 적용해 중복제거 가능
output = list(set(map(tuple, inputs)))
output.sort(key=lambda x:(x[1], x[0]))

for i in range(len(output)):
    print(output[i][0])