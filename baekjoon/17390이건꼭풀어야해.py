import sys

n, q = map(int, sys.stdin.readline().split())

a = list(map(int, sys.stdin.readline().split()))

a.sort()

dp = [0]

for i in range(n):
	dp.append(a[i] + dp[i])

for i in range(q):
	l, r = map(int, sys.stdin.readline().split())
	print(dp[r] - dp[l-1])
