N = int(input())
towers = list(map(int, input().split()))

stack = []
res = []

for idx, height in enumerate(towers):
    while stack:
        if stack[-1][1] > height:  # 스택의 top에 있는 탑의 높이가 현재 탑의 높이보다 클 경우
            res.append(stack[-1][0] + 1)  # 스택의 top에 있는 탑의 인덱스 저장
            break
        stack.pop()
    
    # 스택이 비어있다면 신호를 수신하는 탑이 없다는 의미
    if not stack:
        res.append(0)
    
    # 현재 탑을 스택에 추가
    stack.append((idx, height))

print(' '.join(map(str, res)))
