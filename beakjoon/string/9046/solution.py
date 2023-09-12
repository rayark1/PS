# 테스트 케이스 개수 입력
T = int(input())

for _ in range(T):
    # 문장 입력
    sentence = input()

    # 알파벳 빈도수를 저장할 딕셔너리 초기화
    char_count = {}

    # 문장에서 알파벳 빈도수 계산
    for char in sentence:
        if char.isalpha():  # 알파벳인 경우에만 처리
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

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

    # 결과 출력
    print(most_frequent_char)
