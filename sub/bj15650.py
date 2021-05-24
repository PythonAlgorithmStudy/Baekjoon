n, m = map(int, input().split()) # input().split()을 하면 값을 두 개 받을 수 있다.

a = [] # 빈 리스트 생성
def rec():
    if len(a) == m: # 리스트 길이가 m 길이와 같으면 출력
        b = a[:]
        b.sort()
        print(*b)
        return # 재귀
 
    for i in range(1, n+1): # 'a' 리스트 안에 수열 만들기
        if i in a:
            continue # 리스트 내부의 중복 방지
        a.append(i)
        rec() # 재귀 호출
        a.pop() # 재귀가 끝나면 사용한 리스트 요소 삭제

rec()

# 재귀 호출의 알고리즘이 어떻게 진행되는지 많이 헷갈리고 어려웠다. 
# 특히 return 후의 과정이 이해가 어려웠다.
# 또한 map, split 같은 함수 사용법을 잘 몰랐는데 알게 되었다.