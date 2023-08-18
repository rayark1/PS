import sys

T = int(sys.stdin.readline().rstrip())
results = []

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    results.append(A + B)
# 출력
for result in results:
    print(result)