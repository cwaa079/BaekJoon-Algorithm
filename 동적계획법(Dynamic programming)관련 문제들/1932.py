#https://www.acmicpc.net/problem/1932
#간단한 dp 문제

def solution(n, graph):
    for i in range(1, n):
        for j in range(len(graph[i])):
            if j == 0:
                graph[i][j] += graph[i-1][j]
            elif j == len(graph[i]) - 1:
                graph[i][j] += graph[i-1][j-1]
            else:
                graph[i][j] += max(graph[i-1][j-1], graph[i-1][j])
    return max(graph[n-1])

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

print(solution(n, graph))
