# 비밀번호 발음하기

## 배운 점

- 예외 조건을 먼저 return False로 처리하고, 그 외의 조건을 return True로 처리하는 것이 코드를 간결하게 만든다.

- list나 string과 in 연산자를 사용하면 코드를 간결하게 만들 수 있다.

- any 함수를 사용하면 코드를 간결하게 만들 수 있다.

```python
def check_quality(password):
    vowels = "aeiou"
    
    # 조건 1: 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
    if not any(v in password for v in vowels):
        return False
    
    # 조건 2: 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
    vowel_count = 0
    consonant_count = 0
    for char in password:
        if char in vowels:
            vowel_count += 1
            consonant_count = 0
        else:
            consonant_count += 1
            vowel_count = 0

        if vowel_count == 3 or consonant_count == 3:
            return False

    # 조건 3: 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
    for i in range(len(password)-1):
        if password[i] == password[i+1] and password[i] not in ["e", "o"]:
            return False

    return True
```

## 문제

- 회사 FnordCom은 그런 패스워드 생성기를 만들려고 계획중이다. 당신은 그 회사 품질 관리 부서의 직원으로 생성기를 테스트해보고 생성되는 패스워드의 품질을 평가하여야 한다. 높은 품질을 가진 비밀번호의 조건은 다음과 같다.

- 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
이 규칙은 완벽하지 않다;우리에게 친숙하거나 발음이 쉬운 단어 중에서도 품질이 낮게 평가되는 경우가 많이 있다.

## 입력

- 입력은 여러개의 테스트 케이스로 이루어져 있다.

- 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 테스트할 패스워드가 주어진다.

- 마지막 테스트 케이스는 end이며, 패스워드는 한글자 이상 20글자 이하의 문자열이다. 또한 패스워드는 대문자를 포함하지 않는다.

## 출력

- 각 테스트 케이스를 '예제 출력'의 형태에 기반하여 품질을 평가하여라.
