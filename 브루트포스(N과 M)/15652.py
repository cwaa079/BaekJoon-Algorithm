#https://www.acmicpc.net/problem/15652
#N과 M(4)

def solution(n, m):
    s = []
    
    def dfs(start):
        if len(s) == m:
            print(' '.join(map(str, s)))
            return

        for i in range(start, n+1):
            s.append(i)
            dfs(i)
            s.pop()

    return dfs(1)

n, m = map(int, input().split())
solution(n, m)
