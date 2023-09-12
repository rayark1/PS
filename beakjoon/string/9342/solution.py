import re

def is_infected(chromosome):
    # 정규식 패턴 설정
    pattern = r'^[A-F]?A+F+C+[A-F]?$'
    # 패턴이 일치하는지 확인
    if re.match(pattern, chromosome):
        return True
    return False

# 테스트 케이스 개수 입력
t = int(input())

# 각 테스트 케이스에 대해 확인
for _ in range(t):
    chromosome = input().strip()
    if is_infected(chromosome):
        print("Infected!")
    else:
        print("Good")
