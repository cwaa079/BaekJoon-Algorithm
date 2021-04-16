#https://www.acmicpc.net/problem/17143
#낚시왕
#pypy3제출

import sys
input = sys.stdin.readline

r, c, m = map(int, input().split()) #행열, 상어의 수
graph = [[0]*c for _ in range(r)] #상어의 정보

for i in range(m):
    R, C, s, d, z = map(int, input().split())
    graph[R-1][C-1] = [s, d-1, z] #속력, 방향, 크기

dx = [-1, 1, 0, 0] #위아래오른쪽왼쪽
dy = [0, 0, 1, -1]

def move_shark():
    temp = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if graph[i][j] != 0:
                x, y, s, d, z = i, j, graph[i][j][0], graph[i][j][1], graph[i][j][2]
                while s > 0:
                    x += dx[d]
                    y += dy[d]
                    if 0 <= x < r and 0 <= y < c:
                        s -= 1
                    else:
                        x -= dx[d]
                        y -= dy[d]
                        if d == 0: d = 1
                        elif d == 1: d = 0
                        elif d == 2: d = 3
                        elif d == 3: d = 2
                if temp[x][y] == 0:
                    temp[x][y] = [graph[i][j][0], d, z]
                else:
                    if temp[x][y][2] < z:
                        temp[x][y] = [graph[i][j][0], d, z]
    return temp

total = 0 #최종 낚은 상어의 합
for j in range(c):
    for i in range(r):
        if graph[i][j] != 0: #가장 가까운 상어
            total += graph[i][j][2] #크기 합
            graph[i][j] = 0 #해당 위치의 상어는 잡힘
            break
    graph = move_shark()

print(total)
