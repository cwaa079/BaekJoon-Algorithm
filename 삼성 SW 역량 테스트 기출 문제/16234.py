#https://www.acmicpc.net/problem/16234
#인구이동
#BFS문제

from collections import deque

n, l, r = map(int, input().split()) #크기, 인구차이 l이상 r이하
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0] #상좌하우
dy = [0, -1, 0, 1]

def bfs(x, y, index): #해당하는 국가의 모든 연합을 체크한뒤 데이터 갱신
    united = []
    united.append((x, y)) #연합을 이루는 국가들
    q = deque() #인접한 노드
    q.append((x, y))
    union[x][y] = index #연합의 번호 새김
    sum_union = graph[x][y] #현재 연합의 전체 인구 수
    cnt = 1 #현재 연합 국가의 수

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r: #인구차가 조건과 맞다면
                    q.append((nx, ny)) #다음 국가의 행선지
                    union[nx][ny] = index #연합표시
                    sum_union += graph[nx][ny]
                    cnt += 1
                    united.append((nx, ny))
    #연합 국가끼리 인구 분배
    for i, j, in united:
        graph[i][j] = sum_union // cnt

total = 0 #총 인구이동의 횟수
while True:
    union = [[-1]*n for _ in range(n)] #연합이름
    index = 0 #연합번호
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1: #처리되지 않은 나라라면
                bfs(i, j, index)
                index += 1
    if index == n*n: #모든 인구이동이 끝났다면
        break
    total += 1

print(total)
