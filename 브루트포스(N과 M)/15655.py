#https://www.acmicpc.net/problem/15655
#N과 M(6)

def solution(n, m, arr):
    arr.sort()
    num = []
    def dfs(start):
        if len(num) == m:
            print(' '.join(map(str, num)), end=" ")
            print()
            return

        for i in range(start, n):
            num.append(arr[i])
            dfs(i+1)
            num.pop()

    return dfs(0)


n, m = map(int, input().split())
arr = list(map(int, input().split()))
solution(n, m, arr)
