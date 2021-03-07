n,m = map(int, input().split())

num=[] #숫자들을 넣어 줄 빈 리스트를 만든다.

def f():
    if len(num) == m: #만약 리스트 길이와 m이 같다면
        print(' '.join(map(str,num))) #리스트 num을 문자열로 만든 후 각 숫자들을 ' '로 이어준다.
        return

    for i in range(1,n+1):
        if i in num: #만약 지금 만나고 있는 숫자가 리스트 num에 있다면
            continue #건너뛴다. 즉 i가 0이었다면 1로 바뀐다.
        num.append(i) #그리고 그 숫자를 num에 push 해주고
        f() #위의 행위를 반복한다. 
        #ex) n, m = 4,2라고 했을 때
        #현재 num에는 아무것도 들어가 있지 않으므로 if문을 건너뛰고, for문에 들어온다.
        #1. i=1
        #1은 num에 없으므로 num.append(1)이 수행된다.
        #그리고 f()을 만나 다시 if문부터 시작한다.
        #len(num) = 1이고, m=2이므로 건너뛰고 for문으로 들어온다.
        #i는 1부터 시작하는데 1은 현재 num안에 들어와 있으므로 i=2가 된다.
        #그리고 num.append(2)가 수행되고 f()을 만나 다시 if문부터 시작한다.
        #현재 len(num)은 2이므로 if문이 수행되고
        #print(' '.join(map(str,[1,2])))
        #--> [1,2]이 ['1', '2']가 되고 다시 join에 의해 1 2가 되어 출력한다.
        num.pop()
        #pop을 만나 가장 끝에 있는 숫자, 여기서는 2가 삭제되고 
        #i는 3이 되어 위의 과정을 반복한다.

f()