#https://www.acmicpc.net/problem/15683
#감시
#DFS
#pypy로 제출

import sys
from copy import deepcopy
input = sys.stdin.readline

def fill(x, y, cctv_d, arr): #cctv 범위 확인하는 함수
    for i in cctv_d:
        nx, ny = x, y
        while True:
            nx += dx[i]
            ny += dy[i]
            if 0 <= nx < n and 0 <= ny < m: #맵 안에 있을 때
                if arr[nx][ny] == 6: #빈칸이면 확인
                    break
                elif arr[nx][ny] == 0: #벽이면 종료
                    arr[nx][ny] = '#'
            else:
                break

def dfs(arr, cnt):
    global min_value
    temp = deepcopy(arr) #현재의 감시상태

    if cnt == cctv_cnt: #dfs의 깊이와 cctv개수와 같으면
        num = 0
        for i in range(n): #0개수 찾기
            num += temp[i].count(0)
        min_value = min(num, min_value)
        return

    x, y, cctv_N = cctv_info[cnt] #저장되어 있는 cctv 정보 꺼내오기
    for i in cctv[cctv_N]: #cctv 번호에 맞는 위치
        fill(x, y, i, temp) #cctv가 볼 수 있는 범위 표시
        dfs(temp, cnt+1) #현재상태와 그다음 cctv
        temp = deepcopy(arr) #재귀로 가기 전 상태의 배열로 temp복귀

n, m = map(int, input().split()) #사무실 크기
graph = [] #사무실 정보 입력
for i in range(n):
    graph.append(list(map(int, input().split())))

#북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cctv = [ [], [[0], [1], [2], [3]], [[1, 3], [0, 2]],
         [[0, 1], [1, 2], [2, 3], [3, 0]], [[3, 0, 1], [0, 1, 2], [1, 2, 3], [2, 3, 0]],
         [[0, 1, 2, 3]] ] #cctv 번호에 따른 감시할 수 있는 모든 위치

cctv_cnt = 0
min_value = 1e9
cctv_info = [] #모든 cctv 정보 [x,y,cctv번호]

for i in range(n):
    for j in range(m):
        if graph[i][j] != 0 and graph[i][j] != 6:
            cctv_info.append([i, j, graph[i][j]])
            cctv_cnt += 1
dfs(graph, 0)
print(min_value)
