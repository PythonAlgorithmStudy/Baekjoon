import sys

N = str(sys.stdin.readline()) # map으로 하
raw = list(N)
arr = raw[:-1] # \n까지 배열의 요소로 인식되어서(시스템단의 입력이어서 그런 것으로 추정중)

result = sorted(arr, reverse=True)

for i in result:
    print(i, end="")
