#greedy
#2839설탕배달
#hyeyeon-sun님 풀이

weight = int(input())

answer = -1

maxFive = weight // 5

for fiveNum in range(maxFive, -1, -1): #5개 봉지를 한개 씩 줄여가며 3개 봉지 늘리기
    if weight % 5 == 0:
        answer = fiveNum
        break
    remain = weight - 5 * fiveNum
    if remain % 3 != 0:
        continue
    else:
        threeNum = remain // 3
        answer = fiveNum + threeNum
        break

print(answer)