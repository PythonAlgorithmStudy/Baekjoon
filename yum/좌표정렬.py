n=int(input())

L=[]

for l in range(n):
    x, y = map(int, input().split())
    L.append((x,y))


##좌표 정렬하기 1

for x in L :
    print(x[0], x[1])



##좌표 정렬하기 2

for l in range(n):
    x, y = map(int, input().split())
    L.append((y,x))

L=sorted(L)
for x in L:
    print(x[1], x[0])

# while len(L)!=0:
#     min=(100000,100000)
        
#     for b in L:
#         if b[0] < min[0] or b[1] < min[1]:
#             min=(b[0],b[1])

#     print(min[0], min[1])
#     L.remove(min)