n,m = map(int, input().split())

num=[] 

def f():
    if len(num) == m: 
        print(' '.join(map(str,num))) 
        return

    for i in range(1,n+1):
        if i in num:
            continue
        if len(num) !=0:
            if i < max(num):
                continue
        num.append(i)
        f()
        num.pop()
       
f()