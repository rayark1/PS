# 소수 판별 방법

- 소수를 판별하는 가장 기본적인 방법은 2부터 해당 숫자의 제곱근까지의 모든 숫자로 해당 숫자를 나누어 봅니다. 만약 나누어 떨어지는 숫자가 있으면 그 수는 소수가 아닙니다. 이 방법은 주어진 숫자가 n일 때, O(√n)의 시간 복잡도를 가집니다.

```python
def is_prime(num):
    """주어진 숫자가 소수인지 판별하는 함수"""
    if num < 2:  # 2 미만의 숫자는 소수가 아님
        return False
    for i in range(2, int(num**0.5) + 1):  # 2부터 num의 제곱근까지
        if num % i == 0:  # num이 i로 나누어 떨어지면 소수가 아님
            return False
    return True  # 위의 조건을 모두 통과하면 소수
```

- 위의 방법은 주어진 숫자가 n일 때, O(√n)의 시간 복잡도를 가집니다. 하지만 이 방법은 주어진 숫자가 매우 클 경우에는 시간이 오래 걸립니다. 따라서 주어진 숫자가 매우 클 경우에는 다른 방법을 사용해야 합니다.

## 에라토스테네스의 체

- 에라토스테네스의 체는 주어진 숫자 n이 소수인지 판별할 때, 2부터 √n까지의 모든 숫자로 나누어 보는 것이 아니라, 2부터 시작하여 2의 배수를 모두 제거하고, 다음에 남아 있는 수 중에서 가장 작은 수인 3의 배수를 모두 제거하는 방법을 반복하여, 남아 있는 수들이 모두 소수가 되었을 때, 그 수들을 소수로 판별하는 방법입니다.

- 에라토스테네스의 체는 주어진 숫자가 n일 때, O(nloglogn)의 시간 복잡도를 가집니다.

1. 2부터 시작해서 특정 숫자 n까지의 모든 숫자를 나열합니다.
2. 가장 작은 숫자 2는 소수입니다. 2의 배수를 모두 제거합니다.
3. 다음으로 가장 작은 숫자 3은 소수입니다. 3의 배수를 모두 제거합니다.
4. 이러한 방식으로 n까지 반복하면, 남아있는 숫자들이 소수입니다.

```python
def sieve_of_eratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    primes = []
    for p in range(2, n):
        if prime[p]:
            primes.append(p)
    return primes

print(sieve_of_eratosthenes(30))
# 출력: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

## 소수 판별 알고리즘 비교

- 특정 숫자 하나가 소수인지 판별하고 싶을 때: is_prime 함수가 효율적입니다.
​
- 특정 범위 내의 모든 소수를 찾고 싶을 때: 에라토스테네스의 체가 효율적입니다. 예를 들어, 1부터 1,000,000까지의 모든 소수를 찾기 위해서는 에라토스테네스의 체가 훨씬 빠르게 동작합니다.