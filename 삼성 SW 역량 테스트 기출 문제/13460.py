#https://www.acmicpc.net/problem/13460
#구슬탈출2
#memory : 31716KB
#time : 104ms

from collections import deque
n, m = map(int, input().split()) #가로, 세로

#상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#방문정보
visit = [[[[False]*m for i in range(n)]for i in range(m)]for i in range(n)]

#현재 구슬, 맵 정보
graph = [list(input().rstrip()) for _ in range(n)]

def move(x, y, nx, ny): #이동하는 함수
    cnt = 0
    while graph[x+nx][y+ny] != "#" and graph[x][y] != "O":
        x += nx
        y += ny
        cnt += 1
    return x, y, cnt #이동후 좌표, 횟수

def bfs():
    while queue:
        rx, ry, bx, by, dis = queue.popleft()
        if dis >10: #무한반복
            break
        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i]) #붉은 구술
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i]) #파란 구슬

            if graph[nbx][nby] != "O": #파란 구슬이 구멍이 아니면
                if graph[nrx][nry] == "O" : #붉은 구슬이 구멍에 빠지면
                    print(dis)
                    return
                if nrx == nbx and nry == nby: #같은 위치에 구슬이 있다면
                    if rcnt > bcnt: #붉은 구슬이 더 많이 움직였다면
                        nrx -= dx[i] #붉은 구슬이 뒤에
                        nry -= dy[i]
                    else: #파란 구슬이 더 많이 움직였다면
                        nbx -= dx[i] #파랑 구슬이 뒤에
                        nby -= dy[i]
                if not visit[nrx][nry][nbx][nby]:
                    visit[nrx][nry][nbx][nby] = True
                    queue.append([nrx, nry, nbx, nby, dis+1])
    print(-1)

#각 구슬 위치 알아내기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R': #빨간색 구슬
            rx, ry = i, j
        if graph[i][j] == 'B': #파란색 구슬
            bx, by = i, j

queue = deque()
queue.append([rx,ry,bx,by,1]) #붉은구슬, 파란구슬 좌표, 방향을 바꾼 횟수
visit[rx][ry][bx][by] = True
bfs()
