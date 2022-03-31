#https://www.acmicpc.net/problem/11724
#연결 요소의 개수
def solution(n,m,temp):
    graph = [[] for _ in range(n+1)]
    for i in temp:
        a,b = i
        graph[a].append(b)
        graph[b].append(a)

    cnt = 0
    visited = [False] * (n+1)

    def dfs(v):
        visited[v] = True
        for i in graph[v]:
            if visited[i] is False:
                dfs(i)

    for i in range(1, n+1):
        if visited[i] is False:
            cnt += 1
            dfs(i)
    return cnt

n,m = map(int, input().split())
temp = []

'''
프로그래머스와 같은 입력 환경을 구성하기 위해 배열로 입력 받음.
'''
for i in range(m):
    temp.append(list(map(int,input().split())))
    
print(solution(n,m,temp))
