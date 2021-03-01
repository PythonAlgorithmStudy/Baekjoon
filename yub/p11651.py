import sys
N = int(sys.stdin.readline())
dots = [[0]*2 for i in range(100001)]
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    dots[i][0] = x
    dots[i][1] = y
inputs = dots[:N]

inputs.sort(key=lambda x: (x[1], x[0]))

for i in range(N):
    print(f"{inputs[i][0]} {inputs[i][1]}")