#반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    #1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n + 1):
        result *= i
        print(i, "번째,", n, "값 iterative")
    return result

#재귀적으로 구현한 n!
def factorial_recursive(n):
    print(n, "값 recursive")
    if n <= 1:      #n이 1 이하인 경우 n을 반환
        return n
    #n! = n * (n - 1)!를 그대로 코드로 작성하기
    return n * factorial_iterative(n - 1)

#각각의 방식으로 구현한 n! 출력(n = 5)
print('반복적으로 구현:', factorial_iterative(5))
print('재귀적으로 구현:', factorial_recursive(5))