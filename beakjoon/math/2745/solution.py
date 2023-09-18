# 알파벳 대문자와 그에 해당하는 10진수 값을 매핑하기 위한 딕셔너리
char_to_num = {
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
    'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21,
    'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27,
    'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33,
    'Y': 34, 'Z': 35
}

# B진법 수 N을 10진법으로 변환하는 함수
def convert_to_decimal(N, B):
    decimal_value = 0
    N = N[::-1]  # 문자열을 뒤집어서 더 작은 자리수부터 처리
    
    for i in range(len(N)):
        # 현재 자리의 문자가 알파벳이라면, 해당하는 숫자로 변환
        if 'A' <= N[i] <= 'Z':
            value = char_to_num[N[i]]
        # 그렇지 않으면 그대로 숫자로 변환
        else:
            value = int(N[i])
        # 변환된 값에 B의 i 거듭제곱을 곱해 10진법 값에 더함
        decimal_value += value * (B ** i)
    
    return decimal_value

# 입력받기
N, B = input().split()
B = int(B)

# 결과 출력
print(convert_to_decimal(N, B))
