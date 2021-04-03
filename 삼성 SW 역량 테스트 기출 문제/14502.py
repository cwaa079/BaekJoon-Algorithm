#https://www.acmicpc.net/problem/14502
#연구소
#DFS로 풀이했으나 시간초과로 pypy제출

from sys import stdin
input = stdin.readline

n, m = map(int, input().split()) #지도의 크기
graph = [list(map(int, input().split())) for _ in range(n)]
temp = [[0]*m for _ in range(n)] #벽을 세운후의 지도 정보

dx = [-1, 1, 0, 0] #상하좌우
dy = [0, 0, -1, 1]

#바이러스를 전파시키는 함수(DFS)
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

max_value = -1

def get_score():
    s = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                s+=1
    return s

def dfs(count):
    global max_value
    if count == 3: #벽 3개를 세우면
        for i in range(n):
            for j in range(m):
                temp[i][j] = graph[i][j]
        for i in range(n): #바이러스 전파
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        max_value = max(max_value, get_score()) #안전영역 카운트
        return #돌아가기

    #벽 세우는 과정
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                dfs(count)
                graph[i][j] = 0
                count -= 1

dfs(0)
print(max_value)
