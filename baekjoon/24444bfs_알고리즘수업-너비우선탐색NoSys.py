#sys 안 써서 시간초과
from collections import deque

n, m, start = map(int, input().split())

link = [[] for _ in range(n + 1)]

visited = [False for _ in range(n + 1)]
count = [0 for _ in range(n + 1)]

for _ in range(m):
    node1, node2 = map(int, input().split())
    link[node1].append(node2)
    link[node2].append(node1)

for item in link:
    item.sort()

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