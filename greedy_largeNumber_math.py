#greedy
#large number with math

n, m, k = map(int, input().split()) #memorize
numbers = list(map(int, input().split())) #memorize

numbers.sort()
first = numbers[n - 1]
second = numbers[n - 2]

cnt = m // (k + 1)

#The first one is counted k times more.
#Think about remains when m is divided by k
result = first * (cnt * k + (m % (k + 1))) + second * cnt
    
print(result)