# 문자열 게임 2

## 배운 점

- 어떤 문자를 정확히 K개를 포함하는 가장 짧은 연속 문자열의 길이를 구한다.

```python
def find_min_sequence_length(W, K, target_char):
    """
    주어진 문자열 W에서 target_char가 연속된 K번 등장하는 부분 문자열 중 가장 짧은 길이를 반환.
    """
    left, right, count = 0, 0, 0 # count: 현재 left ~ right 구간에 등장한 target_char의 개수
    min_sequence_length = float('inf')
    
    while right < len(W) and left <= right:
        if W[right] == target_char:
            count += 1
        while count == K and left <= right:
            min_sequence_length = min(min_sequence_length, right - left + 1)
            if W[left] == target_char:
                count -= 1
            left += 1
        right += 1

    return min_sequence_length
```

- 어떤 문자를 정확히 K개를 포함하고, 문자열의 첫 번째와 마지막 글자가 해당 문자로 같은 가장 긴 연속 문자열의 길이를 구한다.

```python
def find_max_sequence_length(W, K, target_char):
    """
    주어진 문자열 W에서 target_char가 연속된 K번 등장하는 부분 문자열 중 가장 긴 길이를 반환.
    """
    occurrences = [i for i, c in enumerate(W) if c == target_char] # target_char가 등장하는 위치들의 리스트
    max_sequence_length = -1
    for i in range(len(occurrences) - K + 1):
        start = occurrences[i] # i번째 등장 위치부터 시작하는 부분 문자열
        end = occurrences[i + K - 1] # i + K - 1번째 등장 위치까지 포함하는 부분 문자열
        max_sequence_length = max(max_sequence_length, end - start + 1)
    return max_sequence_length
```

- 최솟값의 경우 초깃값을 무한대로 설정하고, 최댓값의 경우 초깃값을 음의 값 혹은 무한대로 설정하는 것이 편리하다.

```python
min_sequence_length = float('inf')
max_sequence_length = -1
```

## 문제

- 작년에 이어 새로운 문자열 게임이 있다. 게임의 진행 방식은 아래와 같다.

- 알파벳 소문자로 이루어진 문자열 W가 주어진다.
양의 정수 K가 주어진다.
어떤 문자를 정확히 K개를 포함하는 가장 짧은 연속 문자열의 길이를 구한다.
어떤 문자를 정확히 K개를 포함하고, 문자열의 첫 번째와 마지막 글자가 해당 문자로 같은 가장 긴 연속 문자열의 길이를 구한다.
위와 같은 방식으로 게임을 T회 진행한다.

## 입력

- 문자열 게임의 수 T가 주어진다. (1 ≤ T ≤ 100)

- 다음 줄부터 2개의 줄 동안 문자열 W와 정수 K가 주어진다. (1 ≤ K ≤ |W| ≤ 10,000)

## 출력

- T개의 줄 동안 문자열 게임의 3번과 4번에서 구한 연속 문자열의 길이를 공백을 사이에 두고 출력한다.

- 만약 만족하는 연속 문자열이 없을 시 -1을 출력한다.

[문제 원본 링크](https://www.acmicpc.net/problem/20437)
