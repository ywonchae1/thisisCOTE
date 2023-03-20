#Implementation
#예제 4-1 상하좌우

def isCorrect(x, y, num):
    if 0 < x <= num and 0 < y <= num:
        return True
    return False

n = int(input())
direction = list(input().split())

nowX, nowY = 1, 1

for dir in direction:
    if dir == 'L' and isCorrect(nowX, nowY - 1, n):
        nowY -= 1
    elif dir == 'R' and isCorrect(nowX, nowY + 1, n):
        nowY += 1
    elif dir == 'U' and isCorrect(nowX - 1, nowY, n):
        nowX -= 1
    elif dir == 'D' and isCorrect(nowX + 1, nowY, n):
        nowX += 1

print(nowX, nowY)