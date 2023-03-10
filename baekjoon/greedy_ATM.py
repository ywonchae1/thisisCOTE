n = int(input())
time = list(map(int, input().split()))

time.sort()

result = 0
for i in time:
    result += i * n
    n -= 1

print(result)