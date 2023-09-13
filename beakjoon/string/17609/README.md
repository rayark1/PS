# 회문

## 배운 점

- 회문(回文) 또는 팰린드롬(palindrome)은 앞 뒤 방향으로 볼 때 같은 순서의 문자로 구성된 문자열을 말한다.

- 시작 인덱스와 끝 인덱스를 가지고 회문인지 확인하는 함수를 만들어서 사용하면 편하다.

```python
def is__palindrome(s, start, end):
    """회문인지 확인하는 함수"""
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True
```

- 회문이 아닌 경우에는 어느 한 문자를 삭제하여 회문이 되는지 확인한다.

```python
# 현재 포인터가 가리키는 두 문자가 다를 경우
if s[start] != s[end]:
    # 왼쪽 문자를 제거했을 때와 오른쪽 문자를 제거했을 때의 회문 여부 확인
    is_palindrome_after_left_removal = is_palindrome(s, start + 1, end)
    is_palindrome_after_right_removal = is_palindrome(s, start, end - 1)
    
    # 두 경우 중 하나라도 회문이면 유사 회문
    if is_palindrome_after_left_removal or is_palindrome_after_right_removal:
        return 1
```

## 문제

- 회문(回文) 또는 팰린드롬(palindrome)은 앞 뒤 방향으로 볼 때 같은 순서의 문자로 구성된 문자열을 말한다. 예를 들어 ‘abba’ ‘kayak’, ‘reviver’, ‘madam’은 모두 회문이다. 만일 그 자체는 회문이 아니지만 한 문자를 삭제하여 회문으로 만들 수 있는 문자열이라면 우리는 이런 문자열을 “유사회문”(pseudo palindrome)이라고 부른다. 예를 들어 ‘summuus’는 5번째나 혹은 6번째 문자 ‘u’를 제거하여 ‘summus’인 회문이 되므로 유사회문이다.

- 여러분은 제시된 문자열을 분석하여 그것이 그 자체로 회문인지, 또는 한 문자를 삭제하면 회문이 되는 “유사회문”인지, 아니면 회문이나 유사회문도 아닌 일반 문자열인지를 판단해야 한다. 만일 문자열 그 자체로 회문이면 0, 유사회문이면 1, 그 외는 2를 출력해야 한다.

## 입력

- 입력의 첫 줄에는 주어지는 문자열의 개수를 나타내는 정수 T(1 ≤ T ≤ 30)가 주어진다. 다음 줄부터 T개의 줄에 걸쳐 한 줄에 하나의 문자열이 입력으로 주어진다. 주어지는 문자열의 길이는 3 이상 100,000 이하이고, 영문 알파벳 소문자로만 이루어져 있다.

## 출력

- 각 문자열이 회문인지, 유사 회문인지, 둘 모두 해당되지 않는지를 판단하여 회문이면 0, 유사 회문이면 1, 둘 모두 아니면 2를 순서대로 한 줄에 하나씩 출력한다.

[문제 원본 링크](https://www.acmicpc.net/problem/17609)
