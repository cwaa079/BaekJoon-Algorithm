#https://www.acmicpc.net/problem/2468
#안전영역
#DFS - 재귀제한

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0] #상우하좌
dy = [0, 1, 0, -1]

def dfs(x, y, depth, visited): #안전영역 구하는 함수
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<n and visited[nx][ny] is False:
            if graph[nx][ny] > depth:
                visited[nx][ny] = True
                dfs(nx, ny, depth, visited)

def sol():
    answer = -1e9
    for d in range(max(map(max, graph))): #주어진 배열에서 가장 큰 값까지만 반복
        cnt = 0
        visited = [[False] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if graph[i][j] > d and visited[i][j] is False:
                    visited[i][j] = True
                    cnt += 1
                    dfs(i, j, d, visited)
        answer = max(answer, cnt)
    print(answer)

sol()
