#https://www.acmicpc.net/problem/15649
#N과 M(2)

def solution(n, m):
    s = []

    def dfs():
        if len(s) == m:
            print(' '.join(map(str, s)))
            return
        for i in range(1, n + 1):
            if i not in s:
                s.append(i)
                dfs()
                s.pop()

    return dfs()


n, m = map(int, input().split())
solution(n, m)
