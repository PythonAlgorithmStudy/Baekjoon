def is_empty(stack):
    if(len(stack) <= 0):
        print("1")
        return 1
    else:
        print("0")
        return 0

def stack_push(stack, x):
    stack.append(x)

def stack_pop(stack):
    if(len(stack) <= 0):
        print("-1")
        return;
    last = stack.pop()
    print(last)

def stack_size(stack):
    print(len(stack))

def stack_top(stack):
    if(len(stack) < 1):
        print("-1")
        return;
    top = stack[-1]
    print(top)

N = int(input())
orders = []
for _ in range(N):
    order = str(input())
    orders.append(order)

stack = []
top = 0
for i in orders:
    split_order = i.split() # 띄어쓰기 기준으로 나눌때 (push x 구분용)
    if(len(split_order) > 1):
        stack_push(stack, split_order[1])
    elif(i == "pop"):
        stack_pop(stack) 
    elif(i == "size"):
        stack_size(stack)
    elif(i == "empty"):
        is_empty(stack)
    else:
        stack_top(stack)
