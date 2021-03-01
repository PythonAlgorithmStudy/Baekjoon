import sys
N = int(sys.stdin.readline())
members = [[0]*3 for i in range(100001)]
for i in range(N):
    x, y = sys.stdin.readline().split()
    members[i][0] = int(x)
    members[i][1] = str(y)
    members[i][2] = i
inputs = members[:N]

inputs.sort(key=lambda x: (x[0], x[2]))
for j in range(N):
    print(f"{inputs[j][0]} {inputs[j][1]}")