n=int(input())

L=[]
c=0
for _ in range(n):
    a, b= input().split()
    a=int(a)
    c+=1
    L.append((a, b, c))

L = sorted(L, key=lambda x:(x[0], x[-1]))
for x in L :
    print(x[0], x[1])
