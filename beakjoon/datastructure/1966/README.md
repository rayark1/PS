# 프린터 큐

## 배운 점

- deque을 사용하여 문제에 접근한다.

- deque을 생성할 때, 튜플로 해당 문서의 중요도와 인덱스를 저장한다.

```python
# 문서의 중요도를 입력받고, 각 문서를 (중요도, 인덱스) 형태로 큐에 넣습니다.
docs = deque((val, idx) for idx, val in enumerate(map(int, input().split())))
```

- 문서의 중요도를 확인하고, 해당 문서의 중요도보다 큰 문서가 있는지 확인한다.

```python
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
```

## 문제

- 여러분도 알다시피 여러분의 프린터 기기는 여러분이 인쇄하고자 하는 문서를 인쇄 명령을 받은 ‘순서대로’, 즉 먼저 요청된 것을 먼저 인쇄한다. 여러 개의 문서가 쌓인다면 Queue 자료구조에 쌓여서 FIFO - First In First Out - 에 따라 인쇄가 되게 된다. 하지만 상근이는 새로운 프린터기 내부 소프트웨어를 개발하였는데, 이 프린터기는 다음과 같은 조건에 따라 인쇄를 하게 된다.

- 현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.

- 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.
예를 들어 Queue에 4개의 문서(A B C D)가 있고, 중요도가 2 1 4 3 라면 C를 인쇄하고, 다음으로 D를 인쇄하고 A, B를 인쇄하게 된다.

- 여러분이 할 일은, 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다. 예를 들어 위의 예에서 C문서는 1번째로, A문서는 3번째로 인쇄되게 된다.

## 입력

- 첫 줄에 테스트케이스의 수가 주어진다. 각 테스트케이스는 두 줄로 이루어져 있다.

- 테스트케이스의 첫 번째 줄에는 문서의 개수 N(1 ≤ N ≤ 100)과, 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M(0 ≤ M < N)이 주어진다. 이때 맨 왼쪽은 0번째라고 하자. 두 번째 줄에는 N개 문서의 중요도가 차례대로 주어진다. 중요도는 1 이상 9 이하의 정수이고, 중요도가 같은 문서가 여러 개 있을 수도 있다.

## 출력

- 각 테스트 케이스에 대해 문서가 몇 번째로 인쇄되는지 출력한다.