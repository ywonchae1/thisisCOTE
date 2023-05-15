import sys

n = int(input())

x = list(map(int, sys.stdin.readline().split()))
y = sorted(list(set(x)))

dic = {}
for i in range(len(y)):
	dic[y[i]] = i

for j in x:
	print(dic[j], end=' ')
