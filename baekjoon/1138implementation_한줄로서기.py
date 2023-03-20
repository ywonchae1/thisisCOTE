#implementation
#1138 한 줄로 서기

n = int(input())
mem = list(map(int, input().split()))
stack = []
tmp = []

for i in range(n, 0, -1):
    while len(stack) > mem[i - 1]:
        tmp.append(stack.pop())
    stack.append(i)
    while len(tmp) != 0:
        stack.append(tmp.pop())

print(stack)
