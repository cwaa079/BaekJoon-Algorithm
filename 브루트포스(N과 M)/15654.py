#https://www.acmicpc.net/problem/15654
#N과 M(5)

def solution(n, m, arr):
    arr.sort()
    s = []

    def dfs():
        if len(s) == m:
            print(' '.join(map(str, s)))
            return

        for i in arr:
            if i not in s:
                s.append(i)
                dfs()
                s.pop()

    return dfs()


n, m = map(int, input().split())
arr = list(map(int, input().split()))
solution(n, m, arr)
