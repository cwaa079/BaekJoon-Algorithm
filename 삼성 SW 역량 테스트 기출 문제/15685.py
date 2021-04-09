#https://www.acmicpc.net/problem/15685
#드래곤커브
#시뮬레이션 문제
#x,y 좌표 확실히 구분하기 / 개념 이해하면 구현하는데에는 쉬운 문제

import sys
input = sys.stdin.readline

n = int(input()) # 드래콘 커브의 크기
graph = [[0] * 101 for _ in range(101)] #드래곤커브 좌표
dcurve = []
for i in range(n):
    y, x, d, g = map(int, input().split()) #좌표, 시작방향, 세대
    dcurve.append([x, y, d, g])

dx = [0, -1, 0, 1]#우상좌하
dy = [1, 0, -1, 0]

for curve in dcurve:
    x, y, d, g = curve
    graph[x][y] = 1
    temp = [d] #이전꺼 저장
    q = [d] #세대별 이동방향
    for i in range(g+1):
        for k in q:
            x += dx[k]
            y += dy[k]
            graph[x][y] = 1
        #q 정의
        q = [(j+1)%4 for j in temp]
        q.reverse()
        temp = temp + q

#네 꼭짓점이 드래곤 커브인 경우
cnt = 0
for i in range(100):
    for j in range(100):
        if graph[i][j] and graph[i][j+1] and graph[i+1][j] and graph[i+1][j+1]:
            cnt += 1

print(cnt)
