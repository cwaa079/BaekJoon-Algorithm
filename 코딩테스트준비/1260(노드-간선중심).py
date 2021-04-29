#https://www.acmicpc.net/problem/1260
#DFS와 BFS
#노드버전으로 코딩

from collections import deque
def dfs(v, visited, graph):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if visited[i] is False:
            dfs(i, visited, graph)


def bfs(v, visited, graph):
    q = deque([v])
    visited[v] = True
    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in graph[now]:
            if visited[i] is False:
                q.append(i)
                visited[i] = True

# 입력부분
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    graph[i].sort()

visited = [False] * (n + 1)


def solution(n, m, v, graph, visited):
    dfs(v, visited, graph)
    print()
    visited = [False] * (n + 1)
    bfs(v, visited, graph)

solution(n,m,v,graph,visited)
