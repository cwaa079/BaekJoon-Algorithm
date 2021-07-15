#https://www.acmicpc.net/problem/2529
#부등호
#dfs/bfs 간단한 문제

def solution(n, a):
    mx, mn = '', ''
    visited = [False] * 10

    def possible(i, j, c):
        if c == '<': return i < j
        if c == '>': return i > j

    def dfs(cnt, s):
        nonlocal mx, mn

        if cnt == n+1:
            if len(mn) == 0: mn = s
            else: mx = s
            return

        for i in range(10):
            if visited[i] == False:
                if cnt == 0 or possible(s[-1], str(i), a[cnt-1]):
                    visited[i] = True
                    dfs(cnt+1, s+str(i))
                    visited[i] = False

    dfs(0, "")
    print(mx)
    print(mn)


n = int(input())
a = list(map(str, input().split()))

solution(n, a)
