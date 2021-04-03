#https://www.acmicpc.net/problem/14503
#로봇 청소기
#BFS로 풀이

import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split()) #크기
r,c,d = map(int, input().split()) #청소기좌표, 방향
graph = [] #정보

dx = [-1, 0, 1, 0] #북동남서
dy = [0, 1, 0, -1]

for i in range(n): #입력
    graph.append(list(map(int, input().split())))

def bfs(x, y, d):
    q = deque([[x, y, d]])
    cnt = 1
    while q:
        x, y, d = q.popleft()
        graph[x][y] = 2
        nd = d
        for i in range(4):
            nd = (nd-1) % 4 #방향
            nx = x + dx[nd]
            ny = y + dy[nd]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny]==0:
                cnt += 1
                graph[nx][ny] == 2
                q.append([nx, ny, nd])
                break
            elif i == 3:
                back = (d - 2) % 4
                nx = x + dx[back]
                ny = y + dy[back]

                if graph[nx][ny] == 1:
                    return cnt
                else:
                    q.append([nx, ny, d])

print(bfs(r,c,d))
