from collections import Counter

# 입력
N = int(input())
numbers = [int(input()) for _ in range(N)]

# 산술평균
mean = round(sum(numbers) / N)

# 중앙값
sorted_numbers = sorted(numbers)
median = sorted_numbers[N // 2]

# 최빈값
freqs = Counter(numbers)
most_common = freqs.most_common()
if len(most_common) > 1 and most_common[0][1] == most_common[1][1]:
    mode = most_common[1][0]
else:
    mode = most_common[0][0]

# 범위
range_val = sorted_numbers[-1] - sorted_numbers[0]

# 출력
print(mean)
print(median)
print(mode)
print(range_val)
