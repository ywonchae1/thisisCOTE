#greedy
#make one

n, m = map(int, input().split())

cnt = 0
while n != 1:
    cnt += 1
    if n % m != 0:
        n -= 1
    else:
        n /= m
        
print(cnt)