#https://www.acmicpc.net/problem/16236
#아기 상어
#단순한 bfs를 이용한 시뮬레이션 문제

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())  # 크기
graph = []  # 물고기 정보
for i in range(n):
    graph.append(list(map(int, input().split())))

shark_size = 2  # 아기상어 크기
shark_x, shark_y = 0, 0  # 아기상어 위치

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            graph[i][j] = 0
            shark_x, shark_y = i, j

dx = [-1, 0, 1, 0]  # 상우하좌
dy = [0, 1, 0, -1]


def bfs():  # 모든 위치까지의 최단 거리만 계산
    dist = [[-1] * n for _ in range(n)]  # 최단거리계산
    q = deque([(shark_x, shark_y)])
    dist[shark_x][shark_y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if dist[nx][ny] == -1 and graph[nx][ny] <= shark_size:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    return dist


def find(dist):  # 먹을 물고기를 찾는 함수
    x, y = 0, 0
    min_dist = 1e9
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and 1 <= graph[i][j] < shark_size:  # 상어크기보다 작은 물고리라면
                if dist[i][j] < min_dist:  # 최솟값 갱신
                    x, y = i, j  # 최솟값의 위치
                    min_dist = dist[i][j]
    if min_dist == 1e9:
        return None
    else:
        return x, y, min_dist


t = 0  # 먹을 수 있는 시간
cnt = 0  # 가능한 물고기 개수

while True:
    value = find(bfs())  # 먹을 수 있는 물고기의 위치 찾기, 걸리는 시간

    if value == None:  # 먹을 물고기가 없으면
        print(t)
        break
    else:
        shark_x, shark_y = value[0], value[1]
        t += value[2]
        graph[shark_x][shark_y] = 0  # 먹은 위치에는 아무 것도 없음
        cnt += 1  # 먹은 개수
        if cnt >= shark_size:  # 먹은 개수가 크면
            shark_size += 1
            cnt = 0
