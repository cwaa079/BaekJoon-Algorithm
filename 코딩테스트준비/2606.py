#https://www.acmicpc.net/problem/2606
#바이러스
#DFS

n = int(input()) #컴퓨터 개수
m = int(input()) #연결되어 있는 컴퓨터쌍의 개수
graph = [[0] * (n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

visited = [False] * (n+1) #방문여부 체크

def dfs(i):
    global cnt
    visited[i] = True
    for j in range(1, n+1):
        if graph[i][j] == 1 and visited[j] is False:
            cnt += 1
            dfs(j)

cnt = 0
dfs(1)
print(cnt)
