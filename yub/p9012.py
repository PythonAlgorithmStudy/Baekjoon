T = int(input())

lines = []
for _ in range(T):
    test_case = str(input())
    lines.append(test_case)

# (이면 담고, )이면 stack에서 꺼내기
for i in lines:
    # 하나의 test_case마다 스택, flag 초기화
    stack = []
    flag = 0
    for j in i:
        if(j == "("):
            stack.append(1)
        else:
            # (가 하나도 없을 때
            if(len(stack) < 1):
                flag = 1
                break
            else:
                stack.pop()

    if(len(stack) > 0):
        print("NO")
    # stack이 비어있긴 한데 )가 빈 스택에서 나와서 NO인 경우
    elif(flag == 1):
        print("NO")
    else:
        print("YES")