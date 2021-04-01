#dfs 방식으로 풀이
#핵심은 하나의 좌표를 두고 가깝게 4방향으로 모두 검사하면서 가장 큰 값 찾기 + 'ㅜ'모양 예외처리
#visited 처리 유의

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
d = [ (-1, 0), (0, 1), (1, 0), (0, -1)] #상우하좌

def dfs(x, y, value, cnt):
    global max_value

    if cnt==4:
        max_value = max(max_value, value)
        return

    for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]

        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False:
            visited[nx][ny] = True
            dfs(nx, ny, value+paper[nx][ny], cnt+1)
            visited[nx][ny] = False
        else:
            continue

def extra(x,y, value): #ㅜ모양은 예외처리
    global max_value
    if 0<=x-1 and 0<=y+2<m: #ㅗ
        value = paper[x][y]+paper[x][y+1]+paper[x][y+2]+paper[x-1][y+1]
    if 0<=x+1<n and 0<=y+2<m: #ㅜ
        value = paper[x][y]+paper[x][y+1]+paper[x][y+2]+paper[x+1][y+1]
    if 0<=x+2<n and 0<=y+1<m: #ㅏ
        value = paper[x][y]+paper[x+1][y]+paper[x+2][y]+paper[x+1][y+1]
    if x+1<n and 0<=x-1 and 0<=y+1<m: #ㅓ
        value = paper[x][y]+paper[x-1][y+1]+paper[x][y+1]+paper[x+1][y+1]

    max_value = max(max_value, value)

visited = [[False] * m for _ in range(n)]
max_value = -1

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i,j,paper[i][j],1)
        visited[i][j] = False
        extra(i,j,paper[i][j])

print(max_value)
