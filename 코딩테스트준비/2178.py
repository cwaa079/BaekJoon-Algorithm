#https://www.acmicpc.net/problem/2178
#BFS

from collections import deque

n, m = map(int, input().split()) #크기
graph = [] #미로 정보 입력
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 0, 1, 0] #상우하좌
dy = [0, 1, 0, -1]

visited = [[False]*m for _ in range(n)] #방문한지의 여부
temp = [[0]*m for _ in range(n)] #방문한 경로

def bfs(x, y):
    q = deque([[x, y]])
    visited[x][y] = True
    temp[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == False:
                if graph[nx][ny] == 1:
                    temp[nx][ny] = temp[x][y] + 1
                    visited[nx][ny] = True
                    q.append([nx, ny])

bfs(0, 0)
print(temp[n-1][m-1])
