#greedy
#11399ATM
#수학적 접근

n = int(input())
time = list(map(int, input().split()))

time.sort()

result = 0
for i in time:
    result += i * n
    n -= 1

print(result)