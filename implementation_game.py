#Implementation
#실전문제 게임 개발

n, m = map(int, input().split())
#맵 저장소 초기화, 컴프리헨션 문법
d = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turnLeft():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turnTime = 0
while True:
    turnLeft()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turnTime = 0
        continue
    else:
        turnTime += 1
    if turnTime == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turnTime = 0

print(count)