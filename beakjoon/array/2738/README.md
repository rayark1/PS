# 행렬 덧셈

## 배울 점

- 리스트 컴프리헨션을 사용하면 코드가 더 간결해진다.

``` python
matrix_A = [list(map(int, input().split())) for _ in range(N)]
matrix_B = [list(map(int, input().split())) for _ in range(N)]

matrix_C = [[matrix_A[i][j] + matrix_B[i][j] for j in range(M)] for i in range(N)]
```

- 리스트 앞에 *을 붙이면 리스트를 풀어준다. (unpacking)

``` python
for row in matrix_C:
    print(*row)
```

## 문제

두 N×M 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.

## 입력

첫째 줄에 행렬의 크기 N 과 M이 주어진다. 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다. 이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다. N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.

## 출력

첫째 줄부터 N개의 줄에 행렬 A와 B를 더한 행렬을 출력한다. 행렬의 각 원소는 공백으로 구분한다.

## 예제 입력 1

``` plaintext
3 3
1 1 1
2 2 2
0 1 0
3 3 3
4 4 4
5 5 100
```

## 예제 출력 1

``` plaintext
4 4 4
6 6 6
5 6 100
```

[문제 원본 링크](https://www.acmicpc.net/problem/2738)
