k = int(input()) # 정수k 주어주기

stack = [] # 스택을 담을 빈리스트 만들기

for _ in range(k): # k번째만큼 반복
    num = int(input()) # 정수 주어주기
    if num != 0: 
        stack.append(num) # 0이 아니면 stack에 append (제일 끝에 삽입)
    else:
        stack.pop() # 0이면 stack에서 끝에 것 pop
print(sum(stack)) # 합계
