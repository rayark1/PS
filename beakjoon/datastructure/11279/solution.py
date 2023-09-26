import heapq, sys
input = sys.stdin.readline
N = int(input())

heap = []
for _ in range(N):
    integer = int(input())
    if integer == 0:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, -integer)