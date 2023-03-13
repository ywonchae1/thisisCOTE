#greedy
#2839설탕배달
#hyeyeon-sun님 풀이
#develop? But slow?

weight = int(input())
    
answer = -1
    
maxFive = weight // 5
    
if weight % 5 == 0:
    print(maxFive)
    exit()
else:
    for fiveNum in range(maxFive, -1, -1):
        remain = weight - 5 * fiveNum
        if remain % 3 != 0:
            continue
        else:
            threeNum = remain // 3
            answer = fiveNum + threeNum
            break
        
print(answer)