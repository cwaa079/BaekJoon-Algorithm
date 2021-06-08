#https://www.acmicpc.net/problem/10971
#pypy3로 제출

def solution(n, cost):
    min_s = 1e9

    def dfs(start, v, visited, value):
        nonlocal min_s
        if len(visited) == n:
            if cost[v][start] != 0:
                min_s = min(min_s, value + cost[v][start]) #돌아오는 코드 추가
            return

        for i in range(n):
            if cost[v][i] != 0 and i not in visited:
                visited.append(i)
                value += cost[v][i]
                dfs(start, i, visited, value)
                value -= cost[v][i]
                visited.pop()

    for i in range(n):
        dfs(i, i, [i], 0)

    return min_s

n = int(input())
cost = [[0] * n for _ in range(n)]
for i in range(n):
    cost[i] = list(map(int, input().split()))
print(solution(n, cost))
