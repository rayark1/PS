def find_min_sequence_length(W, K, target_char):
    """
    주어진 문자열 W에서 target_char가 연속된 K번 등장하는 부분 문자열 중 가장 짧은 길이를 반환.
    """
    left, right, count = 0, 0, 0 # count: 현재 left ~ right 구간에 등장한 target_char의 개수
    min_sequence_length = float('inf')
    
    while right < len(W) and left <= right:
        if W[right] == target_char:
            count += 1
        while count == K and left <= right:
            min_sequence_length = min(min_sequence_length, right - left + 1)
            if W[left] == target_char:
                count -= 1
            left += 1
        right += 1

    return min_sequence_length

def find_max_sequence_length(W, K, target_char):
    """
    주어진 문자열 W에서 target_char가 연속된 K번 등장하는 부분 문자열 중 가장 긴 길이를 반환.
    """
    occurrences = [i for i, c in enumerate(W) if c == target_char] # target_char가 등장하는 위치들의 리스트
    max_sequence_length = -1
    for i in range(len(occurrences) - K + 1):
        start = occurrences[i] # i번째 등장 위치부터 시작하는 부분 문자열
        end = occurrences[i + K - 1] # i + K - 1번째 등장 위치까지 포함하는 부분 문자열
        max_sequence_length = max(max_sequence_length, end - start + 1)
    return max_sequence_length

test_cases = int(input())

for _ in range(test_cases):
    W = input().strip()
    K = int(input())
    
    overall_min_length, overall_max_length = float('inf'), -1

    for char in set(W):  # W 문자열에 등장하는 모든 문자들에 대해
        overall_min_length = min(overall_min_length, find_min_sequence_length(W, K, char))
        overall_max_length = max(overall_max_length, find_max_sequence_length(W, K, char))
    
    if overall_min_length == float('inf'):
        print(-1)
    else:
        print(overall_min_length, overall_max_length)
