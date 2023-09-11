# 파이썬 F-String

**파이썬 3.6 이상부터 도입된 F-String**은 문자열 포맷팅을 간편하게 수행하는 기술입니다. F-String은 문자열 내에서 변수나 표현식을 중괄호 `{}` 안에 삽입하여 사용할 수 있습니다. 이를 통해 가독성이 향상되고 코드 작성이 간편해집니다.

## 기본 사용법

F-String을 사용하려면 문자열 앞에 `f` 또는 `F`를 붙이고 중괄호 `{}` 안에 변수나 표현식을 넣습니다.

```python
name = "Alice"
age = 30
message = f"My name is {name} and I am {age} years old."
print(message)
# 출력: "My name is Alice and I am 30 years old."
```

## 형식 지정

F-String은 기본적으로 변수의 타입을 유지합니다. 하지만 형식을 지정하면 타입을 변환할 수 있습니다. 형식 지정은 중괄호 안에 콜론 `:`을 붙이고 그 뒤에 형식을 지정합니다.

```python
name = "Alice"
age = 30
message = f"My name is {name} and I am {age} years old."
print(message)
```
