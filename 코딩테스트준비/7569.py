#https://www.acmicpc.net/problem/7569
#토마토
#BFS, 3차원배열

import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split()) #가로, 세로, 높이
graph = [[] for _ in range(h)]
for i in range(h):
    for j in range(n):
        graph[i].append(list(map(int, input().split())))

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

visited = [[[False for i in range(m)] for i in range(n)] for i in range(h)]

def bfs():
    q = deque()
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if graph[k][i][j] == 1:
                    q.append([i, j, k])
    while q:
        x, y, z = q.popleft()
        visited[z][x][y] = True
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0<=nx<n and 0<=ny<m and 0<=nz<h and visited[nz][nx][ny] is False:
                if graph[nz][nx][ny] == 0:
                    q.append([nx, ny, nz])
                    graph[nz][nx][ny] = graph[z][x][y] + 1  # 개수 세기
                    visited[nz][nx][ny] = True

bfs()

check = True
max_num = 0
for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 0: #해당 토마토가 익지 않았으면
                check = False
            max_num = max(max_num, graph[k][i][j])

if check is False: print(-1)
else: print(max_num-1)
