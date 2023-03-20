#Implementation
#실전문제 왕실의 나이트

n = 8
now = input()
nowX = int(ord(now[0])) - int(ord('a')) + 1 #인덱스 1부터
nowY = int(now[1])

dx = [2, 2, 1, -1, -2, -2, 1, -1]
dy = [-1, 1, 2, 2, -1, 1, -2, -2]

cnt = 0
for i in range(len(dx)):
    if 0 < dx[i] + nowX <= n and 0 < dy[i] + nowY <= n:
        cnt += 1

print(cnt)
