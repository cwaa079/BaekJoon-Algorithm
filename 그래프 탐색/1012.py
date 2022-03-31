#https://www.acmicpc.net/problem/1012
#유기농배추

import sys
sys.setrecursionlimit(100000)
def solution(m,n,k,graph):
    cnt = 0
    dir = [[0,-1],[1,0],[0,1],[-1,0]]
    visited = [[False]*m for _ in range(n)]

    def dfs(x,y):
        visited[x][y] = True
        # print(x,y)
        # print(visited)
        for dx,dy in dir:
            nx, ny = dx + x, dy + y
            if 0<=nx<n and 0<=ny<m and visited[nx][ny] is False:
                if graph[nx][ny] == 1:
                    dfs(nx,ny)

    for i in range(n):
        for j in range(m):
            if visited[i][j] is False and graph[i][j] == 1:
                cnt += 1
                dfs(i, j)

    return cnt

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    for i in range(k):
        a,b = map(int,input().split())
        graph[b][a] = 1
    print(solution(m,n,k,graph))
