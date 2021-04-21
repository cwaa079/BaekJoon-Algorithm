#https://www.acmicpc.net/problem/2644
#촌수계산
#BFS

import sys
from collections import deque
input = sys.stdin.readline

n = int(input()) #전체사람수
p1, p2 = map(int, input().split())
m = int(input())

graph = [[0]*(n+1) for _ in range(n+1)] #관계그래프
for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

visited = [0] * (n + 1)

def bfs(start):
    q = deque([start])

    while q:
        now = q.popleft()
        for i in range(n+1):
            if graph[now][i] == 1 and visited[i] == 0:
                q.append(i)
                visited[i] = visited[now] + 1

bfs(p1)

print(visited[p2] if visited[p2] else -1)
