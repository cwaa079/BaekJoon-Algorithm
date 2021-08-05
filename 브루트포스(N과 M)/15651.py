#https://www.acmicpc.net/problem/15651
#N과 M(3)

def solution(n, m):
    s = []

    def dfs():
        if len(s) == m:
            print(' '.join(map(str, s)))
            return

        for i in range(1, n + 1):
            s.append(i)
            dfs()
            s.pop()

    return dfs()


n, m = map(int, input().split())
solution(n, m)
