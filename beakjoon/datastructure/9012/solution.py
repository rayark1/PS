import sys

input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    ps = input().strip()
    stack = []
    is_vps = True
    for char in ps:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                is_vps = False
                break
            stack.pop()
    
    if stack:
        is_vps = False
        
    print("YES" if is_vps else "NO")
