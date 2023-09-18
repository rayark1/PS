A, B, C, M = map(int, input().split())

# 일한 양과 현재의 피로도 초기화
total_work = 0
fatigue = 0

for _ in range(24): # 하루는 24시간
    # 피로도가 M을 초과하지 않으면서 일을 할 수 있는지 체크
    if fatigue + A <= M:
        total_work += B
        fatigue += A
    else: # 그렇지 않으면 휴식을 취함
        fatigue = max(0, fatigue - C) # 피로도는 0 미만으로 내려가지 않음

print(total_work)
