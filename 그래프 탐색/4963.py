#https://www.acmicpc.net/problem/4963
#섬의개수

import sys

sys.setrecursionlimit(100000)


def solution(w, h, graph):
    cnt = 0
    direction = [[0, -1], [1, 0], [0, 1], [-1, 0], [1,1],[1,-1],[-1,1],[-1,-1]]
    visited = [[False] * w for _ in range(h)]

    def dfs(x, y):
        visited[x][y] = True
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] is False:
                if graph[nx][ny] == 1:
                    dfs(nx, ny)

    for i in range(h):
        for j in range(w):
            if visited[i][j] is False and graph[i][j] == 1:
                dfs(i, j)
                cnt += 1

    return cnt


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0: break
    graph = []  # 지도
    for i in range(h):
        temp = list(map(int, input().split()))
        graph.append(temp)

    print(solution(w, h, graph))
