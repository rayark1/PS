# 약수 찾기
def find_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors

n = int(input())
numbers = list(map(int, input().split()))

# 주어진 수 중 가장 작은 수의 약수를 찾는다.
min_num = min(numbers)
candidates = find_divisors(min_num)

# 후보 약수들이 모든 수의 약수인지 확인한다.
for divisor in candidates:
    if all(num % divisor == 0 for num in numbers):
        print(divisor)