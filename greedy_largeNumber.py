#greedy
#large number

n, m, k = map(int, input().split()) #memorize
numbers = list(map(int, input().split())) #memorize

numbers.sort()
first = numbers[n - 1]
second = numbers[n - 2]

result = 0
while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1
    
print(result)