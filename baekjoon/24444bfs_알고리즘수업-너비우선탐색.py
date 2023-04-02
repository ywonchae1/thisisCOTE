from collections import deque
import sys

n, m, start = map(int, sys.stdin.readline().rstrip().split())

link = [[] for _ in range(n + 1)]

visited = [False for _ in range(n + 1)]
count = [0 for _ in range(n + 1)]

for _ in range(m):
    node1, node2 = map(int, sys.stdin.readline().rstrip().split())
    link[node1].append(node2)
    link[node2].append(node1)

for item in link:
    item.sort()

#매개변수를 안 써도 되는지?
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