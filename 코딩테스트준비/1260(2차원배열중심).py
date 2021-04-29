#https://www.acmicpc.net/problem/1260
#DFS와 BFS
#2차원배열 중심으로 코딩

from collections import deque
def dfs(v, visited, graph):
    visited[v] = True
    print(v, end=' ')
    for i in range(n+1):
        if visited[i] is False and graph[v][i] == 1:
            dfs(i, visited, graph)


def bfs(v, visited, graph):
    q = deque([v])
    visited[v] = True
    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in range(n+1):
            if visited[i] is False and graph[now][i] == 1:
                q.append(i)
                visited[i] = True

# 입력부분
n, m, v = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

visited = [False for _ in range(n + 1)]


def solution(n, m, v, graph, visited):
    dfs(v, visited, graph)
    print()
    visited = [False] * (n + 1)
    bfs(v, visited, graph)

solution(n,m,v,graph,visited)
