#https://www.acmicpc.net/problem/11725
#트리의 부모 찾기
'''
BFS는 가장 가까운 노드부터 방문 -> 그래서 방문할때마다 부모노드 저장
'''

from collections import deque
def solution(n, graph):
    adj = [[] * (n+1) for _ in range(n+1)]
    parent = [0] * (n+1)

    for now in graph:
        a, b = now
        adj[a].append(b)
        adj[b].append(a)

    visited = [False] * (n+1)

    def bfs(start):
        q = deque([start])
        visited[start] = True
        while q:
            x = q.popleft()
            for y in adj[x]:
                if visited[y] is False:
                    visited[y] = True
                    q.append(y)
                    parent[y] = x

    bfs(1)
    for i in range(2, n+1):
        print(parent[i])
    return 0


n = int(input())
graph = [] * n
for i in range(n-1):
    graph.append(list(map(int, input().split())))

solution(n, graph)
