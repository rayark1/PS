# A + B - 4

## 배울 점

- 입력이 더 이상 없을 때까지 반복하는 방법

```python
while True:
    try:
        A, B = map(int, input().split())
        print(A + B)
    except EOFError:
        break
```

- `EOFError`는 입력이 더 이상 없을 때 발생하는 에러이다.

## 문제

두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

## 입력

입력은 여러 개의 테스트 케이스로 이루어져 있다.  
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

## 출력

각 테스트 케이스마다 A+B를 출력한다.

## 예제 입력

``` plaintext
1 1
2 3
3 4
9 8
5 2
```

### 예제 출력

``` plaintext
2
5
7
17
7
```

[문제 원본 링크](https://www.acmicpc.net/problem/10951)
