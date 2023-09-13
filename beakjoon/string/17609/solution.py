def is__palindrome(s, start, end):
    """회문인지 확인하는 함수"""
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

def determine_palindrome_type(s):
    """주어진 문자열의 회문 타입을 판별하는 함수.
    0: 회문
    1: 한 문자를 제거하면 회문이 되는 유사 회문
    2: 회문도 유사 회문도 아닌 문자열
    """
    start, end = 0, len(s) - 1
    
    while start < end:
        # 현재 포인터가 가리키는 두 문자가 다를 경우
        if s[start] != s[end]:
            # 왼쪽 문자를 제거했을 때와 오른쪽 문자를 제거했을 때의 회문 여부 확인
            is_palindrome_after_left_removal = is_palindrome(s, start + 1, end)
            is_palindrome_after_right_removal = is_palindrome(s, start, end - 1)
            
            # 두 경우 중 하나라도 회문이면 유사 회문
            if is_palindrome_after_left_removal or is_palindrome_after_right_removal:
                return 1
            # 두 경우 모두 회문이 아니면 2 반환
            return 2
        start += 1
        end -= 1
    # while 루프가 끝났을 때까지 회문이라면 0 반환
    return 0

# 테스트 케이스 수 입력
T = int(input())
for _ in range(T):
    s = input().strip()
    print(determine_palindrome_type(s))
