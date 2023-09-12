# 복호화

## 배운 점

- 문장에서 가장 많이 나오는 문자를 찾는 문제이다.

- 문자열을 입력받아서, 딕셔너리에 각 문자의 빈도수를 저장한다. 해당 문자가 처음 나올 경우와 그렇지 않은 경우를 나누어서 처리한다.

```python
    # 알파벳 빈도수를 저장할 딕셔너리 초기화
    char_count = {}

    # 문장에서 알파벳 빈도수 계산
    for char in sentence:
        if char.isalpha():  # 알파벳인 경우에만 처리
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
```

- 딕셔너리에서 가장 빈번하게 나타나는 문자를 찾는다. 가장 빈번하게 나타나는 문자가 여러 개일 경우를 고려하여 처리한다.

```python
    # 가장 빈번하게 나타나는 문자와 그 빈도수 초기화
    most_frequent_char = ''
    max_count = 0

    # 가장 빈번하게 나타나는 문자 찾기
    for char, count in char_count.items():
        if count > max_count:
            most_frequent_char = char
            max_count = count
        elif count == max_count:
            most_frequent_char = '?'
```

## 문제

- 알파벳의 빈도수를 체크하고, 가장 빈번하게 나타나는 문자를 출력하는 프로그램을 작성하면 된다.

- 만약 주어진 암호문에서 가장 빈번하게 나타나는 문자가 여러 개일 경우, 그 빈번한 문자 중 어느 것이 평문 알파벳 'e'를 가리키는지 확실하게 알 수 없기 때문에 "모르겠음"을 의미하는 '?'를 출력하면 된다.

## 입력

- 입력의 T(1 ≤ T ≤ 20)는 테스트 케이스로, 입력 제일 상단에 주어진다. 각각의 테스트 케이스는 한 줄마다 소문자와 공백으로 이루어진 영어 문장이 주어진다. 이 문장의 길이는 적어도 1이상이며 255이하다.

## 출력

- 각각의 테스트 케이스에 대해, 가장 빈번하게 나타나는 문자를 출력하거나 빈번
하게 나타나는 문자가 여러 개일 경우 '?'를 출력한다.

[문제 원본 링크](https://www.acmicpc.net/problem/9046)
