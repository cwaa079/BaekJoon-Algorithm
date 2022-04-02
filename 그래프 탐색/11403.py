#https://www.acmicpc.net/problem/11403
#경로찾기
'''
i에서 j로 갈 수 있으면 1 / 없으면 0
그래서 bfs로 최단경로를 일일히 찾음 => 완전탐색
0번에서 0번, 1번, 2번으로 갈 수 있는 걸 찾기 위해 while문(i)안에 for문(j)을 두어서 일일히 찾음.
'''

from collections import deque
def solution(n, graph):

    def bfs(start):
        visited = [0] * n
        q = deque([start])
        while q:
            i = q.popleft()
            for j in range(n):
                if graph[i][j] == 1 and visited[j] == 0:
                    visited[j] = 1
                    q.append(j)
        for i in range(n):
            print(visited[i], end = ' ')
        print()

    for i in range(n):
        bfs(i)

    return 0


n = int(input())
graph = []*n
for i in range(n):
    graph.append(list(map(int, input().split())))

solution(n, graph)
