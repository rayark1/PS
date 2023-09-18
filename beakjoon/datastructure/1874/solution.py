n = int(input())
stack = []
result = []  # 연산 결과를 저장할 리스트

current = 1  # 현재 push할 숫자
possible = True  # 수열을 만들 수 있는지 여부를 나타내는 변수

for _ in range(n):
    num = int(input())
    while current <= num:
        stack.append(current)
        result.append('+')
        current += 1
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        possible = False
        break

if possible:
    for op in result:
        print(op)
else:
    print('NO')