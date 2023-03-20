#greedy
#11399ATM
#hyeyeon-sun님 풀이 공유

length = int(input())
times = list(map(int, input().split()))
times = sorted(times)

print(sum(sum(times[:i+1]) for i in range(length)))