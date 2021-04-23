#https://www.acmicpc.net/problem/2573
#빙산
#bfs

import sys, copy
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0] #상우하좌
dy = [0, 1, 0, -1]

def iceberg(graph): #빙산 녹는 함수
    temp = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                        temp[i][j] = temp[i][j] - 1 if temp[i][j] > 0 else 0
    return temp

def bfs(x, y, visited, graph): #분리되는 거 cnt하는 함수
    q = deque([[x, y]])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 0 and visited[nx][ny] is False:
                visited[nx][ny] = True
                q.append([nx, ny])


def sol():
    y = 0
    graphs = copy.deepcopy(graph)
    while True:
        visited = [[False]*m for _ in range(n)]
        cnt = 0
        y += 1  # 시간
        graphs = copy.deepcopy(iceberg(graphs))  #빙산 녹이고

        #모두 녹았는지 확인하고
        flag = 0 #빙산이 모두 녹았는데 2덩어리이상으로 분리되지 않으면
        for i in graphs:
            flag += i.count(0)
        if flag == n*m: return 0

        #모두 안 녹았으면 현재 몇 덩어리가 있는지 확인하고
        for i in range(n):
            for j in range(m):
                if graphs[i][j] != 0 and visited[i][j] is False:
                    bfs(i, j, visited, graphs)
                    cnt += 1
                    if cnt >= 2: return y  # 2덩어리 이상으로 분리되었으면

print(sol())
