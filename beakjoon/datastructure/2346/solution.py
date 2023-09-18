N = int(input())
balloons = list(enumerate(map(int, input().split()), 1))
result = []
idx = 0

for _ in range(N):
    step = balloons[idx][1]
    result.append(balloons.pop(idx)[0])
    if balloons:
        if step > 0:
            idx = (idx + step - 1) % len(balloons)
        else:
            idx = (idx + step) % len(balloons)

print(" ".join(map(str, result)))
