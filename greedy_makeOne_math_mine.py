#greedy
#make one

n, m = map(int, input().split())

cnt = 0
while n != 1:
    if n % m != 0:
        tmp = n - (n // m) * m
        cnt += tmp
        n -= tmp
    else:
        cnt += 1
        n /= m
        
print(cnt)