def to_decimal(s, base):
    """주어진 진법의 문자열을 10진법 숫자로 변환"""
    try:
        return int(s, base)
    except ValueError:  # 변환이 불가능할 경우 None 반환
        return None

def find_combinations(s1, s2):
    possible_combinations = []

    # 2부터 36진법까지 모두 검사
    for base1 in range(2, 37):
        num1 = to_decimal(s1, base1)
        
        if num1 is None:  # 변환이 불가능한 경우 건너뛴다.
            continue

        for base2 in range(2, 37):
            if base1 == base2:
                continue

            num2 = to_decimal(s2, base2)
            
            if num2 is None:  # 변환이 불가능한 경우 건너뛴다.
                continue
            
            if num1 == num2:
                possible_combinations.append((num1, base1, base2))

    return possible_combinations

# 입력 받기
s1, s2 = input().split()

combinations = find_combbinations(s1, s2)

if not combinations:
    print("Impossible")
elif len(combinations) > 1:
    print("Multiple")
else:
    x, a, b = combinations[0]
    print(x, a, b)
