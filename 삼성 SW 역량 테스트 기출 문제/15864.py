#https://www.acmicpc.net/problem/15684
#사다리놓기
#dfs

import sys
input = sys.stdin.readline

def check(): #사다리 타는 과정(같은 수로 내려가는지)
    for j in range(1, n+1):
        nj = j #현재 j값
        for i in range(1, h+1):
            if graph[i][nj] == 1:
                nj += 1 #오른쪽
            elif graph[i][nj-1] == 1:
                nj -= 1 #왼쪽
        if nj != j:
            return False
    return True

def dfs(num, cnt): #가로선의 최대개수, 현재 재귀함수 깊이
    global min_size
    if min_size != 1e9: return
    if num == cnt:
        if check(): #모든 출발지와 목적지가 같다면
            min_size = cnt #사다리의 최소개수
        return

    for j in range(1, n):
        for i in range(1, h+1):
            if graph[i][j-1] == 0 and graph[i][j+1] == 0 and graph[i][j] == 0: #사다리 조건
                graph[i][j] = 1 #사다리 놓고
                dfs(num, cnt+1) #다음 사다리 놓는 재귀함수
                graph[i][j] = 0
                while i < h: #세로선 기준 쭉 내려감
                    if graph[i][j-1] or graph[i][j+1]:
                        break
                    i += 1

n, m, h = map(int, input().split()) #세로선,가로선,놓을 수 있는 가로선
graph = [[0] * (n+1) for _ in range(h+1)] #사다리정보

for i in range(m):
    a, b = map(int, input().split()) #b와 b+1번을 잇는 a번(세로)위치의 가로선
    graph[a][b] = 1 #사다리가 있는 곳

min_size = 1e9
for i in range(4): #최대 3개이므로 3개까지만 검사
    dfs(i, 0)
    if min_size != 1e9:
        print(min_size)
        break
if min_size == 1e9:
    print(-1)
