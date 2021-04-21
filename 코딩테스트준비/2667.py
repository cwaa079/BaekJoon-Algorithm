#https://www.acmicpc.net/problem/2667
#단지번호붙이기
#DFS

import sys
input = sys.stdin.readline

n = int(input()) #지도의 크기
graph = [] #지도 정보
for i in range(n):
    graph.append(list(input().rstrip()))

dx = [-1, 0, 1, 0] #상우하좌
dy = [0, 1, 0, -1]

visited = [[False]*n for _ in range(n)]
answer = []

def dfs(x, y):
    global cnt
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and visited[nx][ny] == False:
            if graph[nx][ny] == '1':
                cnt += 1
                dfs(nx, ny)

index = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == '1' and not visited[i][j]:
            cnt = 1
            dfs(i, j)
            answer.append(cnt)

print(len(answer))
answer.sort()
for i in answer:
    print(i)
