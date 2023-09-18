from collections import deque

# 테스트 케이스의 수
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    # 문서의 중요도를 입력받고, 각 문서를 (중요도, 인덱스) 형태로 큐에 넣습니다.
    docs = deque((val, idx) for idx, val in enumerate(map(int, input().split())))
    count = 0  # 인쇄 횟수

    while docs:
        # 큐의 맨 앞에 있는 문서가 가장 중요한 문서인지 확인합니다.
        if docs[0][0] == max(docs, key=lambda x: x[0])[0]:
            count += 1
            importance, idx = docs.popleft()
            # 인쇄된 문서의 인덱스가 M과 같다면 결과를 출력하고 반복을 종료합니다.
            if idx == M:
                print(count)
                break
        else:
            docs.append(docs.popleft())
