n=int(input())

voca_list=[]

for _ in range(n):
    voca=input()
    voca_list.append(voca)

voca_list = list(set(voca_list)) #중복 제거

voca_list.sort(key=lambda x:(len(x), x))

for x in voca_list:
    print(x)