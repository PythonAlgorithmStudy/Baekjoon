import sys
import itertools  
N, M = map(int, sys.stdin.readline().split())

arr = list(range(N + 1))[1:]
result = list(itertools.combinations_with_replacement(arr, M))
for i in range(len(result)):
    for j in range(M):
        print(result[i][j], end=" ")
    print(end="\n")