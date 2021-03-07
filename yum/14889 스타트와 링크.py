#지역변수: 함수 안에서 만들어진 변수
#전역변수: 함수 밖에서 만들어진 변수
#global: 함수 안에서 전역변수를 만듦 
# ex) global e -> 함수 밖에서도 e라는 변수를 사용할 수 있음

from itertools import combinations
#combination: 조합; 순서의 관계없이 r개의 배열로 나타냄.

n=int(input()) #인원수 받아냄

L=[]
for x in range(n):
    a= list(map(int, input().split())) 
    L.append(a)
#L[n]는 n번 사람이 자기 자신을 제외한 사람들과의 능력치

num = [i for i in range(n)] #0~사람 수-1이 담긴 리스트를 만듦
res = float('inf') #양의 무한대

def f():
    global res #res를 전역변수 만들기

    for cand in combinations(num, n//2):
        #num 리스트에서 n//2개를 뽑아 조합을 만듦
        #4명이라면 2개를 뽑고, 6명이라면 3개를 뽑음

        start = list(cand) #위의 조합에서 뽑은 번호
        link = list(set(num) - set(cand)) #위의 조합에서 뽑히지 않은 번호
        #리스트에서 -(빼기) 연산을 할 수 없으므로 집합으로 바꿔서 차집합을 구한다.

        start_comb = list(combinations(start, 2)) #start에 속한 사람 2명을 뽑고
        link_comb=list(combinations(link, 2)) #link에 속한 사람 2명을 뽑는다.

        start_sum = 0
        for x, y in start_comb:
            start_sum += (L[x][y] + L[y][x])

        link_sum = 0
        for x, y in link_comb:
            link_sum += (L[x][y] + L[y][x])

        if (res > abs(start_sum - link_sum)):
            res = abs(start_sum-link_sum)

f()
print(res)


        
#https://hwiyong.tistory.com/307