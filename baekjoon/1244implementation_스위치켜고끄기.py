# implementation
# 1244 스위치 켜고 끄기

cntLight = int(input())
lights = list(map(int, input().split()))
cntStudent = int(input())


def change(index):
    global lights
    if lights[index] == 0:
        lights[index] = 1
    else:
        lights[index] = 0


for i in range(cntStudent):
    gender, number = map(int, input().split())
    if gender == 1:  # 남자
        nextNum = number #이걸 따로 만들어야.
        while nextNum <= cntLight: #여긴 등호가 들어가야 마지막 스위치 접근 가능
            change(nextNum - 1)
            nextNum += number #number += number로 했더니 9 -> 18 -> 27이 아닌 9 -> 18 -> 36이 됨
    elif gender == 2:  # 여자
        change(number - 1)
        for j in range(1, cntLight):
            left, right = number - 1 - j, number - 1 + j
            if left < 0 or right >= cntLight:
                break
            if lights[left] == lights[right]:
                change(left)
                change(right)
            else:
                break

for k in range(cntLight):
    print(lights[k], end="")
    if (k + 1) % 20 == 0:
        print()
    else:
        print(" ", end="")