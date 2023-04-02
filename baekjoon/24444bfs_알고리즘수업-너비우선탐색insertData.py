#시간초과 코드
from collections import deque
import sys

n, m, start = map(int, sys.stdin.readline().rstrip().split())

link = [[] for _ in range(n + 1)]

visited = [False for _ in range(n + 1)]
count = [0 for _ in range(n + 1)]

def insertData(array, num):
    for i in range(len(array)):
        if array[i] > num:
            array.insert(i, num)
            break
    array.append(num)

for _ in range(m):
    node1, node2 = map(int, sys.stdin.readline().rstrip().split())
    insertData(link[node1], node2)
    insertData(link[node2], node1)

def bfs():
    myQueue = deque()
    if visited[start] == False:
        visited[start] = True
        myQueue.append(start)
        cnt = 1
        while myQueue:
            now = myQueue.popleft()
            count[now] = cnt
            cnt += 1
            for next in link[now]:
                if visited[next] == False:
                    visited[next] = True
                    myQueue.append(next)

bfs()

for k in range(1, len(count)):
    print(count[k])
