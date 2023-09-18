from collections import deque

N, K = map(int, input().split())
queue = deque(range(1, N+1))
result = []

while queue:
    for _ in range(K-1):
        queue.append(queue.popleft())  # 맨 앞의 사람을 빼서 맨 뒤로 보냅니다.
    result.append(queue.popleft())     # K번째 사람을 결과 리스트에 추가합니다.

print("<" + ", ".join(map(str, result)) + ">")