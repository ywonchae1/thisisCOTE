import sys
sys.setrecursionlimit(10 ** 6) #런타임 에러 (RecursionError) 해결

testCase = int(input())

#위, 오른쪽, 아래, 왼쪽
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def dfs(row, column, lambs):
    #현재 위치가 #인지, #이면 -으로 바꾸기
    if lambs[row][column] == '#':
        lambs[row][column] = '-'
        #위, 오른쪽, 아래, 왼쪽으로 이동
        for index in range(4):
            nextR = row + dr[index]
            nextC = column + dc[index]
            if 0 <= nextR < rows and 0 <= nextC < columns and lambs[nextR][nextC] == '#':
                dfs(nextR, nextC, lambs)
        #더이상 갈 곳이 없으면 1을 반환하기
        return 1
    else:
        return 0

result = []
for i in range(testCase):
    #지도 만들기
    rows, columns = map(int, input().split())
    myLambs = []
    for j in range(rows):
        myLambs.append(list(input()))

    count = 0
    #(0,0)부터 (rows,columns)까지 반복
    for nr in range(rows):
        for nc in range(columns):
            count += dfs(nr, nc, myLambs)
    result.append(count)

#결과 출력
for element in result:
    print(element)
